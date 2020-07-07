### installs:

    flask = "*"
    flask-restful = "*"
    flask-sqlalchemy = "*"
    psycopg2 = "*"  - not sure if needed
    flask-migrate = "*"

### steps

    set up flask app with flask api
    create model and config with database uri


    export FLASK_APP=<appname>.py
        - allows you to run flask commands
        - flask run - starts app

        <h1>Perform db migrations</h1>
        - flask db init
        - flask db migrate
        - flask db upgrade

        to have server reload with changes you need to include
        FLASK_DEBUG = 1
