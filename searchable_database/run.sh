#!/bin/bash

# ./run.sh import.py
#       or
# ./run.sh search.py

pip install -r requirements.txt

export DB_USER=db_user
export DB_PASS=db_user_pass
export DB_HOST=127.0.0.1
export DB_PORT=6033
export DB_NAME=app_db

python $@