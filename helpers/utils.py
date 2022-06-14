import hashlib
import os
import yaml
from passlib.handlers.pbkdf2 import pbkdf2_sha256


class Mongo:
    DB = os.environ.get('MONGO_DB')
    URI = os.environ.get('MONGO_URI')
    COLLECTION = os.environ.get('MONGO_COLLECTION')


def normpath(path):
    return os.path.normpath(path)


def load_yaml_file(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f.read())


def is_path_value(value):
    """Return True if the the value is a path which starts with path:

    """
    if isinstance(value, str):
        return value.startswith('path:')
    return False


def process_path_value(config_dir, path):
    return normpath(os.path.join(config_dir, path[5:]))


def load_config_from_yaml_file(config_file):
    """Return a dict object which contains Flask-compatible
    configuration. The config_file MUST be given in absolute
    form. Developer may call os.path.join in prior to obtain correct
    config_file.

    """
    if not os.path.isabs(config_file):
        raise Exception('Config file MUST be given in absolute form')
    config_dir = os.path.dirname(config_file)
    config = load_yaml_file(config_file)
    for key in config:
        if is_path_value(config[key]):
            config[key] = process_path_value(config_dir, config[key])
    return config


def update_config_from_environment(config):
    """Merge config with values from environment. Return the config itself
    with updated values.

    """

    for key in config:
        config[key] = os.environ.get(key, config[key])
    return config


def load_config(from_file=None, env=True):
    """Load config from yaml file specified in parameter `from_file`. If a
    value is set in environment, use the value from environment
    instead. yaml file must be given in an absolute path.
    """
    config = {}
    if from_file is not None:
        config = load_config_from_yaml_file(from_file)
    if env:
        return update_config_from_environment(config)
    else:
        return config


def hashsum_password_local(password, user_name):
    """
    has password, salt = md5 of username
    :param password:
    :param user_name:
    :return:
    """
    try:
        m = hashlib.md5()
        m.update(user_name.encode('utf-8'))
        hash = pbkdf2_sha256.encrypt(password, salt=m.hexdigest().encode('utf-8'), rounds=3615)
        return hash[hash.rfind("$") + 1:]
    except Exception as e:
        print(e)
        return None
