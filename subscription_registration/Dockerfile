FROM python:3.12.1-slim as builder

RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Install requirements.in
RUN pip install --no-cache-dir pip-tools
COPY requirements.in .
RUN pip-compile requirements.in && \
    pip-sync requirements.txt

FROM python:3.12.1-slim

# Open http port
EXPOSE 8000
# PYTHONUNBUFFERED Лог сразу пишется в stdout
# PYTHONDONTWRITEBYTECODE Не создаются .pyc файлы (кэш-компиляция), меньше мусора в контейнере
# DEBIAN_FRONTEND=noninteractive Отключает диалоги во время установки пакетов через apt-get
ENV PYTHONUNBUFFERED=1 \ 
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Копирование установленных пакетов из стадии сборки
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Moving application files
WORKDIR /app
COPY . /app

# копирует статику в /app/staticfiles, чтобы потом Nginx мог её отдать
# RUN python ./manage.py collectstatic --noinput
