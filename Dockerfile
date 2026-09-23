FROM python:3.14-slim
WORKDIR /app
COPY app.py index.html questoes.md ./
# Gera o banco já com as 611 questões (e ordem aleatória) durante o build
RUN DATA_DIR=/seed python3 -c "import app; app.init()" && rm questoes.md
ENV SEED_DB=/seed/quiz.db DATA_DIR=/data HOST=0.0.0.0
VOLUME /data
EXPOSE 8765
CMD ["python3", "app.py"]
