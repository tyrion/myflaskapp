===============================
My Flask App
===============================

A flasky app.


Quickstart
----------

::

    git clone https://github.com/sloria/myflaskapp
    cd myflaskapp
    pip install -r requirements/dev.txt
    export MYFLASKAPP_ENV='dev'
    python manage.py createdb
    python manage.py runserver


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``, ``models``, and ``db``.

Development / Production Environments
-------------------------------------

Configuration environements are handled through the MYFLASKAPP_ENV system environment variable.

To switch to the development environment, set ::

    export MYFLASKAPP_ENV="dev"

To switch to the production environment, set ::

    export MYFLASKAPP_ENV="prod"