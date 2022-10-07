# CNAB txt document parser

- m6-s3-teste-tecnico-Backend-Python

## Objective

This projects is a back-end application that you can run localy, send a file(CNAB format) from request and then it reads each line of the file and register the information in the database. As response it returns the objects created in object format.

# Before running

<mark>Activate venv</mark> using

```
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

# How to run it localy using sqlite3/postgresql/docker
Note: the default database is sqlite3, if you want to set postgresql as default, go to settings.py line 94 and uncomment the following ones. And remove the 87-92 lines. 
## Docker

Note: <mark>Add the informations required</mark> in the .env as well as .env example.

Simply run:

Docker desktop:

```
docker compose up
```

Linux:

```
docker-compose up
```

## Sqlite3

Run:

```
./manage.py migrate
./manage.py create_transac_types
./manage.py runserver
```

## PostgreSQL

Note: Read the section note first. To run in your postgresql, you'll need to create the database, and <mark>add the informations required</mark> in the .env as well as .env example.\
\
Run:

```
./manage.py migrate
./manage.py create_transac_types
./manage.py runserver
```
## When done, test it yourself
To access the docs -> http://localhost:8000/docs/ \
Access the http://localhost:8000/upload/ or http://localhost:3000/upload/, depending on what method you are running, and upload the CNAB_example_file.txt to the "File uploaded" field.\
And that's it. DONE!

## To run tests
Note: e2e tests still in devlopment

First, run the Sqlite3 commands and then:
```
./manage.py test
```

## Covarage

 ```
 coverage run ./manage.py test
 coverage report
 # If you want to get the html files for coverage
 coverage html
 ```