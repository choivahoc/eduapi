# Authentication API

## Install 

- pip install -r requirements.txt

## Pre-run set up

- python init_db.py

## Run Command

- python -m application 


## Dev Configuration

- Change config at `config.yaml`
  - If you have a relational DB `(Postgres, MySQL)`, change the `SQLALCHEMY_DATABASE_URI` variable in `config.yaml` to the corresponding DB_URI you have
  - By default, this application will user SQLite as temporary database
  - Certificates and WSO2IS settings can also be configured at `config.yaml`
    
## Documentations
- To have a better understanding what this system's about, take a look at these documentation
  - [Introduction](./docs/Introduction.md)
  - [Workflow](./docs/Auth Flow.md)

    


