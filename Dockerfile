FROM python:latest

WORKDIR /

COPY . ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "app/app.py"]