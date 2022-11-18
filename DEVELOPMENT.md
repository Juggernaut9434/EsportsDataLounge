# DEVELOPMENT.md

Python Version: 3.9.13


## Set up the Database

Using Postgres, via [PgAdmin 4 v6.12](https://www.pgadmin.org/docs/pgadmin4/6.12/release_notes_6_12.html)
for easy setup on GUI.

1. Create a Database
1. Run [create_tables.sql](./setup/create_tables.sql) to create the tables
1. Import [GeneralEsportData.csv](./setup/GeneralEsportData.csv) into the EsportsEarnings Table
1. Add Credentials to [database.ini](./database.ini) so that the web app can connect to the database

## Start / Run Web Application

1. Create virtual environment (venv) with the python3.9.13
2. Activate virtual environment with `venv/bin/activate`
3. `pip install -r requirements.txt`
4. `make run`

To then deactivate virtual environment
`deactivate`

## Tutorial to Flask

- example: https://github.com/pallets/flask/tree/main/examples/tutorial
