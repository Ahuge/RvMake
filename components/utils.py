import imp
import os
import re
import sys

from settings import logger, PATH_RESOLVE_DEPTH, IMPORT_ERROR_RE
from .exception_classes import BuildException, ConfigurationException
from third_party import mock


def resolve_path(path, recurse=True):
    if not os.path.exists(os.path.abspath(path)) and recurse:
        logger.debug("Path does not exists recursing up: %s " % os.path.abspath(path))
        temp_path = path
        depth = 0
        while depth < PATH_RESOLVE_DEPTH:
            temp_path = os.path.dirname(temp_path)
            if os.path.exists(temp_path):
                break
            depth += 1
        if depth >= PATH_RESOLVE_DEPTH:
            raise BuildException("Unable to resolve path %s" % path)
        return_path = temp_path
    elif not os.path.exists(os.path.abspath(path)) and not recurse:
        return_path = os.path.abspath(path)
        try:
            os.makedirs(path)
        except WindowsError as e:
            BuildException(str(e))
    else:
        return_path = os.path.abspath(path)
    return return_path.replace("\\", "/")


def get_driver(driver_name, files):
    possible_drivers = sorted(filter(lambda x: True if driver_name in x else False, files),
                              key=lambda x: len(x))

    if not possible_drivers:
        raise ConfigurationException("Could not find a suitable %s in the list of gathered files:\n\t%s"
                                     % (driver_name, "\n\t".join(files)))
    return possible_drivers[0]

