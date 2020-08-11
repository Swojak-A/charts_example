# Charts Example Repo
Project showing how to implement plotly charts into Django admin with handful of examples (based on **Django 3.1.0** with **PostgreSQL** database).


## Introduction

_Let's assume we run a PokeInstitute and we need to Report some of the fields of interests in Django admin panel..._

To explain how to use charts most effectively we used a fiction entity to exemplify every aspect of chart creation in most natural way possible.
It will be best to follow along chapters of this README with the lecture of corresponding modules.
Every module is self-contained and rely only on models included in `models.py` file in order to avoid handling with over-complicated relations.


## How to start?

1. Create `.env` file in root dir containing following variables:
 * PWD
 * SECRET_KEY
 * POSTGRES_USER
 * POSTGRES_PASSWORD
 * POSTGRES_DB
 * DJANGO_SETTINGS_MODULE
 * DJANGO_DATABASE_URL

Example content of `.env` file:

```
PWD=/home/user/Py_Projects/charts_example
SECRET_KEY=v3ry-s3cr3t
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
DJANGO_SETTINGS_MODULE=app.settings.dev
DJANGO_DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

```

2. Create `static` directory, change its owner to docker group and change its permissions. You can do it inline by:

```bash
sudo mkdir static && sudo chown :docker static && sudo chmod g+rwx static
```

3. Build docker image using command:

```bash
docker-compose build
```

4. Run docker container using command:

```bash
docker-compose up
```

5. You can now access Django admin panel by visiting `localhost:8000/admin` in your web browser of choice.

##### Useful commands

* starting container and logging into it:

You create container on the run and then shell inside runing container:

```bash
docker-compose run --rm web sh
```

* logging into existing container:

Assuming that you have an existing container and you want to directly log into it:

```bash
docker exec -it <container-name> sh
```

* creating development virtual enviroment:

For the purpose of local development you might want to set up virtual enviroment. First you might want to load correct package - in my case it was `sudo apt-get install python3.8-venv`. Now you can create enviroment using `python3.8 -m venv .venv`.

After completion you can activate it using: `source .venv/bin/acticate`. You can now install dependancies using: `pip install -r requirements/base.txt`

* adding pre-commits:

This boilerplate repo is configured to use **pre-commit** hooks to improve quality of code. Pre-commit contains i.a. **black**, **flake** and **mypy** packages. It handles clean code formatting, unused imports and correct typing.

To install it you have to activate virtual env and run `pip install pre-commit`. Now you run all pre-commit package by: `pre-commit run --all-files`


## Chapter 1: Creating simple chart in admin panel

_To Be Updated_


## Chapter 2: Plotly Graph Objects vs. Plotly Express

_To Be Updated_

## Chapter 3: TruncYear

_To Be Updated_

## Chapter 4: TruncHour

_To Be Updated_
