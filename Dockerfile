FROM python:3.11-slim

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY 8_dzhalo.py .

CMD ["python", "8_dzhalo.py"]