import configparser

config = configparser.ConfigParser()
config.read("resource/config.properties")


def get_config(key):
    return config['DEFAULT'][key]