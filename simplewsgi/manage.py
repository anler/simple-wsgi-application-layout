#!/usr/bin/env python
# encoding: utf-8
"""
This is the file that contains repetitive tasks commonly used in python web
development that we will call `actions`.
An action is a function in this same module starting with ``"action_"``
which takes a number of arguments where every argument has a default.  
The type of the default value specifies the type of the argument.

Arguments can then be passed by position or using ``--name=value`` from
the shell.

Because a runserver and shell command is pretty common there are two
factory functions that create such commands:
    
    action_runserver = script.make_runserver(make_app, use_reloader=True)
    action_shell = script.make_shell(lambda: {'app': make_app()})
    
"""
from werkzeug import script

def make_app():
    from wsgi import Application
    return Application()

def make_shell():
    import models
    application = make_app()
    return locals()

# $ ./manage.py --help
# $ ./manage.py runserver localhost 8080 --debugger --no-reloader
# $ ./manage.py runserver -p 4000
action_runserver = script.make_runserver(make_app, use_reloader=True)

# $ ./manage.py shell
action_shell = script.make_shell(make_shell)
# action_initdb = lambda: make_app().init_database()

if __name__ == '__main__':
    script.run()