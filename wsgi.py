import os
from application import create_app
from helpers.utils import load_config

config_file = os.path.join(os.path.dirname(__file__),
                           'config.yaml')
config = None
if os.path.isfile(config_file):
    config = load_config(config_file)

app = create_app(config)
