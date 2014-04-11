import json
import os
from os.path import expanduser
from django.core.exceptions import ImproperlyConfigured

__author__ = 'juanrbonfante'

local_user = expanduser('~')


class ProjectUtils(object):
    secrets = {}
    project_name = None

    def __init__(self, proj):
        self.project_name = proj


    def open_secrets(self, filename, dir_local=local_user):
        with open('{user}/{file}'.format(user=dir_local, file=filename)) as f:
            self.secrets = json.loads(f.read())


    def get_secret(self, setting, secrets=None):
        """Get the secret variable or return explicit exception"""
        try:
            if secrets is not None:
                return secrets[setting]
            return self.secrets[setting]
        except KeyError:
            error_msg = "Set the {0} environment variable".format(setting)


    def get_env_variable(self, var_name):
        """Get the environment variable or return exception"""
        try:
            return os.environ[var_name]
        except KeyError:
            error_msg = "Set the the {} environment variable".format(var_name)
            raise ImproperlyConfigured(error_msg)


    def get_project_env(self, var_name, secret=False):

        if self.project_name is not None:
            formatted = "{proj}_{variable}".format(proj=self.project_name, variable=var_name)
            if secret:
                return self.get_secret(formatted)
            return self.get_env_variable(formatted)
        else:
            error_msg = "No Project Name was found."
            raise ImproperlyConfigured(error_msg)



