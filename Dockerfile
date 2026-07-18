FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN useradd -m admin && chown -R admin:admin /app

USER admin 

EXPOSE 5000

CMD ["python", "app.py"]
