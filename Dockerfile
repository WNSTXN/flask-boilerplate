FROM python:latest

WORKDIR /

COPY main.py ./
COPY requirements.txt ./
COPY app/ ./app/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "main.py"]
