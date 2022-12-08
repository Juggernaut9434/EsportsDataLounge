## Pull the Repository to Local Machine

```sh
git clone git@github.com:Juggernaut9434/EsportsDataLounge.git
```

## Create a Postgres Database Instance

### Install PostgresSQL

1. [Install PostgreSQL](https://www.postgresql.org/download)
1. check CLI is installed with `psql -V`

### Create Database

1. Navigate to `setup/`
1. There is a setup script provided [setup.sh](setup/setup.sh)
1. Run this script, it will create a database, tables, and import data

#### Password for User

By default the password for users are `postgres` but if there are any issues run:

```sh
psql -c "ALTER USER user_name  WITH PASSWORD 'postgres';"
```

### Setup Credentials for back_end

1. Create `database.ini` file that fills out this template to be in main directory

```ini
[postgresql]
host=localhost
dbName=esports
user=
password=
```

## Setup Python 3.11

### (optional) Install Python Environment Manager

1. Install `pyenv` to your machine. [Documentation](https://github.com/pyenv/pyenv#installation)
1. Check Version with `pyenv --version`
1. Navigate to the root directory of the repository
1. `pyenv install 3.11.0`
1. `pyenv local 3.11.0`

### Create Python Virtual Environment

1. `python -m venv venv` will create a virtual environment under application
1. `source venv/bin/activate` will activate the virtual environment

NOTE: to deactivate type `deactivate` in the terminal

### Install Dependencies

1. With the venv activated, run:
 ```sh
 pip install --upgrade pip;
 pip install -r requirements.txt
 ```

## Run the Program

```sh
flask --app src/frontend/hello_world.py
```

Navigate to http://127.0.0.1:5000 or the link provided when ran the app

