import os
import logging
import logging.config
from werkzeug.exceptions import default_exceptions
import connexion
from helpers.utils import load_config
from application import extensions
from application.exceptions import api_error_handler

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
APPLICATION_ROOT = os.path.join(MODULE_DIR, '..')

app_config = None
if app_config is None:
    config_file = os.path.join(APPLICATION_ROOT, 'config.yaml')
    if os.path.isfile(config_file):
        app_config = load_config(config_file)
    else:
        raise Exception('No valid configuration found')


def create_app(config=None):
    """ Create an Flask application instance.

    :param config:
    :return:
    """

    if not config:
        config = app_config

    swagger_file = config.get('SWAGGER_FILE_PATH')

    if swagger_file:
        swagger_dir, swagger_filename = os.path.split(swagger_file)
        options = {"swagger_ui": True}
        app = connexion.App(__name__,
                            specification_dir=swagger_dir, options=options)
        app.add_api(swagger_filename)

    else:
        raise Exception('SWAGGER_FILE_PATH is required in configuration file.')

    flask_app = app.app
    flask_app.config.from_mapping(config)
    flask_app.config['SECRET_KEY'] = os.urandom(24)
    flask_app.instance_path = MODULE_DIR

    configure_app(flask_app)

    return flask_app


def configure_app(app):
    """
    Configure a Flask app
    :param app:
    :param filename:
    :return:
    """
    # configure_log_handlers(app)
    configure_extensions(app)
    configure_exception_handlers(app)


def configure_log_handlers(app):
    """
    Config log
    :param app: flask app
    :return: not return
    """
    logging.config.fileConfig(app.config['LOGGER_CONFIG_PATH'])

    logger = logging.getLogger('root')

    # unify log format for all handers
    for h in logger.root.handlers:
        app.logger.addHandler(h)
    app.logger.setLevel(logger.root.level)

    app.logger.info('Start api services info log')
    app.logger.error('Start api services error log')


def configure_extensions(app):
    """
    :param app: flask app (main app)
    :return:
    """

    # Initialize DB
    if app.config.get('SQLALCHEMY_DATABASE_URI', '') == '':
        sqlite_file = os.path.join(
            APPLICATION_ROOT,
            'data/db.sqlite')
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite_file
    extensions.db.init_app(app)
    extensions.kvsession.init_app(app)
    extensions.action_logger.init_app(app, logging.getLogger('action'))


def configure_exception_handlers(app):
    for exception in default_exceptions:
        app.register_error_handler(exception, api_error_handler)
    app.register_error_handler(Exception, api_error_handler)
