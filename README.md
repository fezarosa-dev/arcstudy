# Quiz Arquitetura de Computadores II

Site de estudo com 611 questões (CRSC04, Prova 01) em ordem aleatória, sem repetição. Você responde, vê na hora se acertou, marca questões, comenta, vê estatísticas e exporta um relatório em JSON.

Você precisa de **uma** destas duas coisas instaladas: **Python 3.9+** *ou* **Docker**. Não precisa de `pip install` (não há dependências).

---

## Passo 1: baixar o projeto

**Opção A, com Git:**
```bash
git clone git@github.com:fezarosa-dev/arcstudy.git
cd arcstudy
```
**Opção B, sem Git:** na página do GitHub clique em **Code → Download ZIP**, extraia e abra a pasta extraída.

---

## Passo 2: instalar o que falta (só uma vez)

Escolha **Python** (mais simples) ou **Docker**.

### Python
| Sistema | Como instalar | Como conferir |
|---|---|---|
| Linux | geralmente já vem. Senão: `sudo apt install python3` (Debian/Ubuntu) ou `sudo dnf install python3` (Fedora) | `python3 --version` |
| Mac | `brew install python` ou baixe em python.org | `python3 --version` |
| Windows | Baixe em https://www.python.org/downloads/ e, no instalador, **marque "Add python.exe to PATH"** | `py -3 --version` |

### Docker
| Sistema | Como instalar | Como conferir |
|---|---|---|
| Linux | https://docs.docker.com/engine/install/ (o serviço precisa estar ligado: `sudo systemctl start docker`) | `docker compose version` |
| Mac / Windows | Instale o **Docker Desktop** (https://www.docker.com/products/docker-desktop/) e **abra o programa** antes de usar | `docker compose version` |

---

## Passo 3: rodar

Abra o terminal **dentro da pasta do projeto** (onde está o `app.py`).

### Linux / Mac
```bash
./start.sh
```
Se der "permissão negada": `chmod +x start.sh` e tente de novo (ou rode `sh start.sh`).

### Windows
- **Jeito fácil:** dê **duplo clique** em `start.bat`.
- **Pelo terminal (cmd ou PowerShell)**, dentro da pasta: `.\start.bat`

O script escolhe sozinho: usa **Docker** se ele estiver instalado e ligado; senão, usa **Python**.
Aparecerá `Iniciando via ... -> http://localhost:8765`. A primeira vez com Docker demora 1 a 2 minutos (constrói a imagem).

## Passo 4: abrir no navegador

Acesse **http://localhost:8765**

Para **parar**: volte ao terminal e aperte **Ctrl+C** (no Windows, fechar a janela do `start.bat` também para).

---

## Escolher como rodar (opções)

| Você quer | Linux / Mac | Windows |
|---|---|---|
| Automático (Docker se tiver, senão Python) | `./start.sh` | `start.bat` |
| Forçar **Docker** | `./start.sh docker` | `start.bat docker` |
| Forçar **Python** | `./start.sh python` | `start.bat python` |

**Sem usar os scripts** (comandos diretos):

| | Linux / Mac | Windows |
|---|---|---|
| Python | `python3 app.py` | `py -3 app.py` (ou `python app.py`) |
| Docker (em primeiro plano) | `docker compose up --build` | `docker compose up --build` |
| Docker (em segundo plano) | `docker compose up -d --build` | `docker compose up -d --build` |
| Parar o Docker | `docker compose down` | `docker compose down` |

## Mudar porta, endereço e local do banco (variáveis de ambiente)

Nenhuma é obrigatória.

| Variável | Padrão | Para que serve |
|---|---|---|
| `PORT` | `8765` | Porta do site (Python e Docker). Se der "porta em uso", troque por outra, ex.: `9000` |
| `HOST` | `127.0.0.1` | Só Python. `0.0.0.0` deixa acessar de outro aparelho da rede (celular): abra `http://IP-DO-PC:8765`. No Docker já é `0.0.0.0` |
| `DATA_DIR` | pasta do projeto | Só Python. Pasta onde fica o `quiz.db` (seu progresso) |
| `SEED_DB` | vazio | Uso interno da imagem Docker (banco pronto para copiar) |

**Como passar a variável, por sistema:**

| Exemplo | Linux / Mac | Windows cmd | Windows PowerShell |
|---|---|---|---|
| Porta 9000 com o script | `PORT=9000 ./start.sh` | `set PORT=9000 && start.bat` | `$env:PORT=9000; .\start.bat` |
| Porta 9000 só Python | `PORT=9000 ./start.sh python` | `set PORT=9000 && start.bat python` | `$env:PORT=9000; .\start.bat python` |
| Acessível na rede | `HOST=0.0.0.0 ./start.sh python` | `set HOST=0.0.0.0 && start.bat python` | `$env:HOST="0.0.0.0"; .\start.bat python` |
| Banco em outra pasta | `DATA_DIR=~/estudos python3 app.py` | `set DATA_DIR=C:\estudos && py -3 app.py` | `$env:DATA_DIR="C:\estudos"; py -3 app.py` |

---

## Como usar o quiz

- Clique na alternativa (ou tecle **A–D**) para responder e ver na hora se acertou; **←/→** navegam; **F** marca a questão.
- Cada questão tem um campo de **comentário** (salva sozinho).
- A aba **Relatório** mostra acertos, erros, marcadas e comentários, com filtros.
- **Exportar JSON** baixa só as questões com que você interagiu.
- **Reiniciar** (no relatório) apaga tudo e sorteia nova ordem.

## Onde o progresso fica salvo

- **Python:** arquivo `quiz.db` (em `DATA_DIR`). Para zerar, apague o arquivo ou use **Reiniciar**.
- **Docker:** volume `quiz-data`. `docker compose down` mantém o progresso; `docker compose down -v` **apaga**.
- Os dois modos têm bancos separados: o progresso de um não aparece no outro.

## Problemas comuns

| Sintoma | Solução |
|---|---|
| `Address already in use` / porta ocupada | Use outra porta: `PORT=9000 ...` (veja a tabela acima) |
| Windows: `python` não é reconhecido | Reinstale o Python marcando **Add to PATH**, ou use `py -3 app.py` |
| `Cannot connect to the Docker daemon` | Ligue o Docker (abra o Docker Desktop, ou `sudo systemctl start docker` no Linux) |
| Linux: `permission denied` no Docker | `sudo usermod -aG docker $USER`, saia e entre na sessão de novo |
| Mudei o código e o Docker não mudou | Rode com `--build` (o `start` já faz isso) |

## Detalhes técnicos

Backend em Python + SQLite (só biblioteca padrão), interface em HTML/CSS/JS puro. O `quiz.db` é criado a partir de `questoes.md` na primeira execução; na imagem Docker ele já vem pronto com as 611 questões.

---
Feito por Zanoni · [www.zanoni.dev.br](https://www.zanoni.dev.br)
