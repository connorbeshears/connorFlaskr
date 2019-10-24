import os
from flask import Flask

# Copied from the Flask website 

def create_app(test_config=None, x=None):
    # create and configure the appl
    appl = Flask(__name__, instance_relative_config=True)
    appl.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(appl.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        appl.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        appl.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(appl.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @appl.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import dbAcc
    dbAcc.init_app(appl)

    from . import auth
    appl.register_blueprint(auth.bp)

    from . import blog
    appl.register_blueprint(blog.bp)
    appl.add_url_rule('/', endpoint='index')

    return appl

