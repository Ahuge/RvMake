import os
import logging

ACCEPTABLE_CONFIG_EXTENSIONS = (
    ".rvcfg",
    ".cfg",
)

INCLUDED_FILE_TYPE = (
    ".py",
    ".mu",
)

PYTHON_INIT = "__init__.py"
PACKAGE_NAME = "PACKAGE_TEMPLATE"
IMPORT_ERROR_RE = "No\smodule\snamed\s(\w+)"
PATH_RESOLVE_DEPTH = 2
LOGGING_FORMAT = "%(name)s: %(filename)s [%(levelname)s]: %(message)s"

logging.basicConfig(format=LOGGING_FORMAT, level=logging.WARNING)
logger = logging.getLogger(os.path.splitext(os.path.basename(os.path.dirname(__file__)))[0])
