FROM python:3.8-slim-buster
WORKDIR /app
ENV FLASK_APP=app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["export", "FLASK_APP=app"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
