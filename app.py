#!/usr/bin/env python3
"""Quiz de estudo: python3 app.py  ->  http://localhost:8765
Lê questoes.md (banco de questões), guarda tudo em quiz.db (SQLite). Só stdlib."""
import json, os, random, re, shutil, sqlite3, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
DATA = Path(os.environ.get("DATA_DIR", ROOT))
DB = DATA / "quiz.db"
SEED = Path(os.environ.get("SEED_DB", ""))  # banco pré-populado embutido na imagem
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", 8765))

SCHEMA = """
CREATE TABLE IF NOT EXISTS questions(id INTEGER PRIMARY KEY, diff TEXT, star INT, text TEXT,
  options TEXT, answer TEXT, topic TEXT, expl TEXT);
CREATE TABLE IF NOT EXISTS ord(pos INTEGER PRIMARY KEY, qid INT UNIQUE);
CREATE TABLE IF NOT EXISTS progress(qid INTEGER PRIMARY KEY, choice TEXT, correct INT,
  flagged INT DEFAULT 0, comment TEXT DEFAULT '', ts REAL);
CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT);
"""


def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def parse(md):
    body, _, tail = md.partition("## Gabarito rápido")
    key = dict(re.findall(r"\*\*(\d+)\*\*-([a-e])", tail.split("## Gabarito comentado")[0]))
    expl = {}
    for m in re.finditer(r"^\| (\d+) \| \*\*(\w)\*\* \| (.*?) \| (.*) \|$", tail, re.M):
        expl[m[1]] = (m[3], m[4])
    out = []
    for m in re.finditer(r"### Questão (\d+) \[(\w)\]( ★)?\n\n(.*?)(?=\n### Questão |\n---\s*$|\Z)", body, re.S):
        n, diff, star, blk = m[1], m[2], bool(m[3]), m[4]
        parts = re.split(r"\n(?=[a-e]\) )", blk.strip())
        opts = {p[0]: p[3:].strip() for p in parts[1:]}
        topic, ex = expl.get(n, ("", ""))
        out.append((int(n), diff, int(star), parts[0].strip(), json.dumps(opts, ensure_ascii=False), key[n], topic, ex))
    return out


def init():
    DATA.mkdir(parents=True, exist_ok=True)
    if not DB.exists() and SEED.is_file():
        shutil.copy(SEED, DB)
    c = db()
    c.executescript(SCHEMA)
    if not c.execute("SELECT 1 FROM questions").fetchone():
        qs = parse((ROOT / "questoes.md").read_text(encoding="utf-8"))
        assert len(qs) == 611 and all(len(json.loads(q[4])) >= 2 for q in qs), "parse falhou"
        c.executemany("INSERT INTO questions VALUES(?,?,?,?,?,?,?,?)", qs)
        shuffle(c)
    c.commit()
    c.close()


def shuffle(c):
    """Ordem aleatória fixa: cada questão aparece uma única vez."""
    ids = [r[0] for r in c.execute("SELECT id FROM questions")]
    random.shuffle(ids)
    c.execute("DELETE FROM ord")
    c.executemany("INSERT INTO ord VALUES(?,?)", enumerate(ids))
    c.execute("INSERT OR REPLACE INTO meta VALUES('pos','0')")


def get_pos(c):
    return int(c.execute("SELECT v FROM meta WHERE k='pos'").fetchone()[0])


def stats(c):
    total = c.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
    r = c.execute("SELECT COUNT(choice) a, COALESCE(SUM(correct),0) h, COALESCE(SUM(flagged),0) f, "
                  "SUM(comment!='') cm FROM progress").fetchone()
    a, h = r["a"], r["h"]

    def group(col):
        return [dict(r) for r in c.execute(
            f"SELECT q.{col} k, COUNT(*) a, SUM(p.correct) h FROM progress p JOIN questions q ON q.id=p.qid "
            f"WHERE p.choice IS NOT NULL GROUP BY q.{col} ORDER BY 1")]

    return dict(total=total, answered=a, hits=h, wrong=a - h, flagged=r["f"], comments=r["cm"] or 0,
                pos=get_pos(c), by_topic=group("topic"), by_diff=group("diff"))


def question(c, pos):
    r = c.execute("SELECT q.*, p.choice, p.correct, p.flagged, p.comment FROM ord o "
                  "JOIN questions q ON q.id=o.qid LEFT JOIN progress p ON p.qid=q.id WHERE o.pos=?", (pos,)).fetchone()
    if not r:
        return None
    d = dict(pos=pos, id=r["id"], diff=r["diff"], star=r["star"], text=r["text"], options=json.loads(r["options"]),
             topic=r["topic"], choice=r["choice"], flagged=bool(r["flagged"]), comment=r["comment"] or "")
    if r["choice"]:  # gabarito só depois de responder
        d.update(correct=bool(r["correct"]), answer=r["answer"], expl=r["expl"])
    return d


def interacted(c):
    """Só questões com interação (respondida, marcada ou comentada); as não vistas são ignoradas."""
    rows = c.execute(
        "SELECT q.id, o.pos+1 AS ordem, q.diff, q.topic, q.text, q.options, q.answer, q.expl, "
        "p.choice, p.correct, p.flagged, p.comment FROM progress p JOIN questions q ON q.id=p.qid "
        "JOIN ord o ON o.qid=q.id WHERE p.choice IS NOT NULL OR p.flagged=1 OR p.comment!='' ORDER BY o.pos")
    return [dict(id=r["id"], ordem=r["ordem"], dificuldade=r["diff"], assunto=r["topic"], pergunta=r["text"],
                 alternativas=json.loads(r["options"]), gabarito=r["answer"], explicacao=r["expl"],
                 resposta=r["choice"], acertou=None if r["choice"] is None else bool(r["correct"]),
                 marcada=bool(r["flagged"]), comentario=r["comment"] or "") for r in rows]


def upsert(c, qid, **f):
    c.execute("INSERT OR IGNORE INTO progress(qid) VALUES(?)", (qid,))
    c.execute("UPDATE progress SET " + ",".join(f"{k}=?" for k in f) + " WHERE qid=?", (*f.values(), qid))


class H(BaseHTTPRequestHandler):
    def send(self, body, ctype="application/json", code=200, extra=None):
        b = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        p = self.path.split("?")[0]
        c = db()
        try:
            if p == "/":
                self.send((ROOT / "index.html").read_bytes(), "text/html")
            elif p == "/api/state":
                self.send(stats(c))
            elif m := re.fullmatch(r"/api/q/(\d+)", p):
                q = question(c, int(m[1]))
                self.send(q or {"error": "fim"}, code=200 if q else 404)
            elif p == "/api/report":
                self.send(interacted(c))
            elif p == "/api/export":
                fn = time.strftime("respostas-%Y%m%d-%H%M.json")
                self.send(json.dumps(interacted(c), ensure_ascii=False, indent=2).encode(),
                          extra={"Content-Disposition": f'attachment; filename="{fn}"'})
            else:
                self.send({"error": "404"}, code=404)
        finally:
            c.close()

    def do_POST(self):
        p = self.path
        d = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
        c = db()
        try:
            if p == "/api/answer":
                r = c.execute("SELECT answer, expl FROM questions WHERE id=?", (d["qid"],)).fetchone()
                done = c.execute("SELECT choice FROM progress WHERE qid=?", (d["qid"],)).fetchone()
                if not r or d.get("choice") not in list("abcde") or (done and done[0]):
                    return self.send({"error": "inválido ou já respondida"}, code=400)
                ok = int(d["choice"] == r["answer"])
                upsert(c, d["qid"], choice=d["choice"], correct=ok, ts=time.time())
            elif p == "/api/flag":
                upsert(c, d["qid"], flagged=int(bool(d["flagged"])))
            elif p == "/api/comment":
                upsert(c, d["qid"], comment=str(d["comment"])[:5000])
            elif p == "/api/pos":
                c.execute("INSERT OR REPLACE INTO meta VALUES('pos',?)", (str(int(d["pos"])),))
            elif p == "/api/reset":  # apaga respostas e sorteia nova ordem
                c.execute("DELETE FROM progress")
                shuffle(c)
            else:
                return self.send({"error": "404"}, code=404)
            c.commit()
            self.send({"ok": True})
        finally:
            c.close()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    init()
    print(f"Quiz em http://localhost:{PORT}")
    ThreadingHTTPServer((HOST, PORT), H).serve_forever()
