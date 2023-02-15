# Searchable DB

This example makes use of sqlalchemy to interact with a mariadb (mysql) database. Phpmyadmin and the database exist in docker containers.


## prereqs

To use this example as-is, you will need docker (https://get-docker.com/) and docker-compose (https://docs.docker.com/compose/install/) and you will also need to install pymysql's prereqs (https://pypi.org/project/PyMySQL/)


## steps
1. terminal 1 `$ docker-compose up` (phpmyadmin available at http://localhost:8080/ root:my_secret_password)
2. termianl 2 - install virtualenv and install requirements
```
$ python3 -m venv venv && . venv/bin/activate
$ pip install -r requirements.txt
$ export DB_USER=db_user
$ export DB_PASS=db_user_pass
$ export DB_HOST=127.0.0.1
$ export DB_PORT=6033
$ export DB_NAME=app_db
$ python3 import.py

> imported 1000
> ./run.sh import.py  3.13s user 0.39s system 49% cpu 7.108 total
```

At this point we have a seeded DB which you can view at http://localhost:8080



3.  termianl 2 - Search (default options)
```
$ python3 search.py
No options selected...
usage: search.py [-h]
                 [--id ID | --age AGE | --age_range AGE_RANGE | --age_range_code AGE_RANGE_CODE | --area_code AREA_CODE | --carrier_route CARRIER_ROUTE | --estimated_home_income ESTIMATED_HOME_INCOME | --estimated_home_value ESTIMATED_HOME_VALUE | --gender GENDER | --first_name FIRST_NAME | --home_value_range HOME_VALUE_RANGE | --housing_type HOUSING_TYPE | --income_range INCOME_RANGE | --income_range_code INCOME_RANGE_CODE | --latitude LATITUDE | --last_name LAST_NAME | --longitude LONGITUDE | --own_or_rent OWN_OR_RENT | --own_or_rent_code OWN_OR_RENT_CODE | --is_homeowner IS_HOMEOWNER | --name_combined NAME_COMBINED | --latitude_fromatted LATITUDE_FROMATTED | --longitude_fromatted LONGITUDE_FROMATTED | --infogroup_id INFOGROUP_ID | --address ADDRESS | --phone PHONE | --city CITY | --county COUNTY | --state_province STATE_PROVINCE | --postal_code POSTAL_CODE | --is_do_not_call IS_DO_NOT_CALL]

Query database

options:
  -h, --help            show this help message and exit
  --id ID               Entity id (INTEGER)
  --age AGE             Entity age (VARCHAR(255))
  --age_range AGE_RANGE
                        Entity age_range (VARCHAR(255))
<snip>
```
4.  termianl 2 - Search (with column and value)
``` 
$ python3 search.py--last_name Taylor
search for last_name: Taylor
{   '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x101fae1a0>,
    'address': '1617 Kinsale Dr',
    'age': '84',
    'age_range': '65+',
    'age_range_code': 'M',
    'area_code': '850',
    'carrier_route': 'R010',
    'city': 'Cantonment',
    'county': 'ESCAMBIA',
    'estimated_home_income': '$90,000 - $99,999',
    'estimated_home_value': '$175,000 - $199,999',
    'first_name': 'Kenneth',
    'gender': 'Male',
    'home_value_range': '$175,000 - $199,999',
    'housing_type': 'Single Family Dwelling',
    'id': 4,
    'income_range': '$90,000 - $99,999',
    'income_range_code': 'I',
    'infogroup_id': 500000150260,
    'is_do_not_call': True,
    'is_homeowner': True,
    'last_name': 'Taylor',
    'latitude': 30.5703,
    'latitude_fromatted': '30.570340',
    'longitude': -87.2703,
    'longitude_fromatted': '-87.270340',
    'name_combined': 'Kenneth Taylor',
    'own_or_rent': 'Confirmed Owner',
    'own_or_rent_code': '3',
    'phone': 'Not Approved',
    'postal_code': '32533',
    'state_province': 'FL'}
{   '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x101fef2e0>,
    'address': '1465 Baytowne Ave E',
    'age': '84',
    'age_range': '65+',
    'age_range_code': 'M',
    'area_code': '850',
    'carrier_route': 'C003',
    'city': 'Miramar Beach',
    'county': 'WALTON',
    'estimated_home_income': '$175,000 - $199,999',
    'estimated_home_value': '$800,000 - $899,999',
    'first_name': 'William',
    'gender': 'Male',
    'home_value_range': '$800,000 - $899,999',
    'housing_type': 'Single Family Dwelling',
    'id': 995,
    'income_range': '$175,000 - $199,999',
    'income_range_code': 'M',
    'infogroup_id': 900013009654,
    'is_do_not_call': True,
    'is_homeowner': True,
    'last_name': 'Taylor',
    'latitude': 30.3897,
    'latitude_fromatted': '30.389710',
    'longitude': -86.3097,
    'longitude_fromatted': '-86.309700',
    'name_combined': 'William Taylor',
    'own_or_rent': 'Confirmed Owner',
    'own_or_rent_code': '3',
    'phone': 'Not Approved',
    'postal_code': '32550',
    'state_province': 'FL'}
```


This example only accepts one column/value pair