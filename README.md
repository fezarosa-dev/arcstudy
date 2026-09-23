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

## Detalhes

- Backend: Python + SQLite (stdlib). Banco `quiz.db` criado a partir de `questoes.md` na primeira execução.
- No Docker o banco já vem pronto na imagem e o progresso fica no volume `quiz-data` (`docker compose down -v` apaga o progresso).
- Porta e endereço: variáveis `PORT`/`HOST` no `app.py`.
