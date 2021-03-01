FROM python:3.9

WORKDIR /flask

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "app.py"]