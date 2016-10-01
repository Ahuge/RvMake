import os
from .exception_classes import BuildException
from settings import PACKAGE_NAME


def load_package():
    directory = os.path.dirname(os.path.dirname(__file__))
    if PACKAGE_NAME not in os.listdir(directory):
        raise BuildException("Could not find internal package template file. Please reinstall...")
    with open(os.path.join(directory, PACKAGE_NAME), "rb") as fh:
        template = fh.read()
    return template
