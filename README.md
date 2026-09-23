# Quiz Arquitetura de Computadores II

Site de estudo com 611 questões (CRSC04, Prova 01) em ordem aleatória, sem repetição. Você responde, vê na hora se acertou, marca questões, comenta, vê estatísticas e exporta um relatório em JSON.

## Como rodar

Escolha um:

```bash
./start.sh          # Linux/Mac: usa Docker se tiver, senão Python
start.bat           # Windows (mesma lógica)
```

Ou manualmente:

```bash
docker compose up --build     # com Docker
python3 app.py                # sem Docker (só precisa do Python 3.9+, sem pip install)
```

Abra **http://localhost:8765**.

## Uso

- Clique na alternativa (ou tecle **A–D**) para responder; **←/→** navegam, **F** marca a questão.
- Cada questão tem um campo de comentário (salva sozinho).
- A aba **Relatório** mostra acertos, erros, marcadas e comentários, com filtros.
- **Exportar JSON** baixa só as questões com que você interagiu.
- **Reiniciar** (no relatório) apaga tudo e sorteia nova ordem.

## Opções e parâmetros

### 1. Modo de execução (argumento do `start`)

| Comando | O que faz |
|---|---|
| `./start.sh` | Automático: usa **Docker** se ele estiver instalado e ligado, senão usa **Python** |
| `./start.sh docker` | Força Docker (`docker compose up --build`) |
| `./start.sh python` | Força Python puro (`python3 app.py`), sem Docker |

No Windows é igual: `start.bat`, `start.bat docker`, `start.bat python`.
Para parar: **Ctrl+C**.

### 2. Variáveis de ambiente

Coloque antes do comando. Nenhuma é obrigatória.

| Variável | Padrão | Para que serve |
|---|---|---|
| `PORT` | `8765` | Porta do site. Vale para Python e para Docker (no Docker é a porta exposta no seu computador) |
| `HOST` | `127.0.0.1` | Endereço de escuta (só Python). Use `0.0.0.0` para acessar de outro aparelho da rede, ex.: celular. No Docker já é `0.0.0.0` |
| `DATA_DIR` | pasta do projeto | Onde fica o `quiz.db` com seu progresso (só Python) |
| `SEED_DB` | vazio | Banco pronto para copiar se o `quiz.db` ainda não existir (usado pela imagem Docker) |

Exemplos:

```bash
PORT=9000 ./start.sh                      # site em http://localhost:9000
PORT=9000 ./start.sh python               # idem, sem Docker
HOST=0.0.0.0 ./start.sh python            # acessível pela rede local
DATA_DIR=~/meus-estudos python3 app.py    # guarda o progresso em outra pasta
```

No Windows (cmd): `set PORT=9000 && start.bat`.

### 3. Onde o progresso fica salvo

- **Python:** no arquivo `quiz.db` (em `DATA_DIR`). Para zerar, apague o arquivo ou use **Reiniciar** no Relatório.
- **Docker:** no volume `quiz-data`. `docker compose down` mantém o progresso; `docker compose down -v` **apaga**.
- Os dois modos têm bancos separados, o progresso de um não aparece no outro.

## Detalhes

- Backend: Python + SQLite (stdlib). Banco `quiz.db` criado a partir de `questoes.md` na primeira execução.
- No Docker o banco já vem pronto na imagem e o progresso fica no volume `quiz-data` (`docker compose down -v` apaga o progresso).
