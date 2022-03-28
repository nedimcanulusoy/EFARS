FROM python:3.10.2-slim-buster

WORKDIR /usr/src/app

COPY . .
RUN rm -rf venv

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]