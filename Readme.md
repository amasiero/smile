# Smile

This project is create for a class about Python using Flask and SQLAlchemy to develop a website.

It was inspired on community school/orphanage problem, which is to receive and to collect donations.

Hope you enjoy it!

## Requirements

To run this project you will need:

- Python 3
- MySQL Community 8

## How to: Install

First, clone it:

```
git clone https://github.com/amasiero/smile.git
```

Access folder and create a Python Virtual Environment:

On Windows:

```
cd smile
python -m venv .\venv
```

On Linux/Mac

```
cd smile
python -m venv ./venv
```

Then activate virtual environment:

On Windows:

```
.\venv\Scripts\activate.bat
```

On Linux/Mac

```
./venv/Scripts/activate
```

Now execute:

```
pip install -r requirements.txt
```

Done! You install it!

## Setup database

Create a .env file and type follow variable:

```
DATABASE_URL='mysql+pymysql://<user>:<password>@<hostname>:<port>/<database>'
```

> Don´t forget to type your´s system info on above url.

<!-- After that execute db_create.py script:

```
python db_create.py
``` -->

Now your database is ready to fly!

## Run project

Execute follow command on terminal:

```
flask run
```

At browser access:
<http://localhost:5000/>

That´s it!

_Red five standing by!_
