FROM python:3.8.10-alpine
WORKDIR /deployment
COPY . /deployment/

RUN pip3 install pipenv
RUN pipenv install -r requirements.txt

CMD [ "pipenv", "run", "python3", "main.py" ]