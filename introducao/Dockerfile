# 1. Máquina com Python
FROM python:3.11.6-slom-bullseye

# 2. Copiar arquivos
WORKDIR /home/app
COPY ./requirements.txt .

# 3. Instalar as dependências
RUN pip install -r requirements.txt

# 4. Copiar arquivos
COPY . .

# 5. Expor a porta
EXPOSE 8000

# 5. Rodar a aplicação
CMD ["fastapi", "dev", "main.py"]
