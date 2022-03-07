import os


class ImproperlyConfigured(Exception):
    pass


def load_environment_variables(env_name):
    """ Get environment variable or raise an Exception """
    try:
        os.environ.get(env_name)
    except KeyError:
        raise ImproperlyConfigured(f"environment variable {env_name} not found")
