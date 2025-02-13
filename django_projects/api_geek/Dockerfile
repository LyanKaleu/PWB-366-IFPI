FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código depois de instalar as dependências
COPY . .

# Rodar migrações e coletar arquivos estáticos antes de iniciar o servidor
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "api_geek.wsgi:application", "--bind", "0.0.0.0:8000"]