

Installation Pre-requisites
============================
1. python 3 installed (with pip)
2. Django/Selenium e.g.
`pip install "django" "selenium"`
3. MySql Client e.g.
`pip install django mysqlclient`

Setup
---------
- Create virtual environment
`python3 -m venv virtualenv`

- Activate env
`source virtualenv/bin/activate`


Running Tests
-------------
- Run Unit Tests
`(virtualenv) kxtractut> $ python manage.py test`


- Launch Server and Run Selenium Function Tests

`(virtualenv) kxtractui> $ python manage.py runserver`

`(virtualenv) kxtractui> $ python functional_tests.py`

**REMEMBER** 

Database password for `ui_readonly` is stored in Env variable cf. settings.py
` 'PASSWORD': os.getenv('DB_RO_PASSWORD'),`



