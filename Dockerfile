FROM python:3.7-slim

WORKDIR /usr/src/app

COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install

COPY bootstrap-ionos-server.py ./

CMD ["pipenv", "run", "python", "./bootstrap-ionos-server.py" ]