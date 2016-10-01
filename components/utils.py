import imp
import os
import re
import sys

from settings import logger, PATH_RESOLVE_DEPTH, IMPORT_ERROR_RE
from .exception_classes import BuildException
from third_party import mock


def resolve_path(path):
    if not os.path.exists(os.path.abspath(path)):
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
    else:
        return_path = os.path.abspath(path)
    return return_path.replace("\\", "/")


def mock_import(mock_name):
    logger.debug("Mocking %s" % mock_name)
    sys.modules[mock_name] = mock.Mock()


def import_driver(file_path):
    directory = os.path.dirname(file_path)
    name = os.path.splitext(os.path.basename(file_path))[0]
    try:
        _file, _pathname, _description = imp.find_module(name, [directory])
    except ImportError as e:
        raise BuildException("Could not import config[\"main\"] file. \"%s\"" % str(e))

    module = None
    try:
        import_error = True
        while import_error:
            try:
                logger.info("Importing driver %s" % _pathname)
                module = imp.load_module(name, _file, _pathname, _description)
                import_error = False
            except ImportError as e:
                match = re.match(IMPORT_ERROR_RE, str(e))
                if not match:
                    raise BuildException("Could not parse import error from parsing %s. %s" % (name, str(e)))
                mock_import(match.group(1))
    except Exception as e:
        raise BuildException("Could not import config[\"main\"] file. \"%s\"" % str(e))
    finally:
        if _file:
            _file.close()
    return module
