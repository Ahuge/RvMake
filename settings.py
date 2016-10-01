import re
import os
import logging
from collections import namedtuple

ACCEPTABLE_CONFIG_EXTENSIONS = (
    ".rvcfg",
    ".cfg",
    ".yaml",
)

INCLUDED_FILE_TYPE = (
    ".py",
    ".mu",
)

PYTHON_INIT = "__init__.py"
PACKAGE_NAME = "PACKAGE_TEMPLATE"
IMPORT_ERROR_RE = re.compile("No\smodule\snamed\s(\w+)")
INIT_FUNCTION_NAME = "self.init"
PATH_RESOLVE_DEPTH = 2
LOGGING_FORMAT = "%(name)s: %(filename)s [%(levelname)s]: %(message)s"
EVENT_KEY_STR = "key-down--"

logging.basicConfig(format=LOGGING_FORMAT, level=logging.WARNING)
logger = logging.getLogger(os.path.splitext(os.path.basename(os.path.dirname(__file__)))[0])

DEFAULT_CONFIG = {
    "author": "",
    "organization": "",
    "contact": "",
    "url": "",
    "requires": "''",
    "icon": "",
    "imageio": [],
    "movieio": [],
    "hidden": False,
    "system": False,
    "optional": False,
    "files": "",
    "menu": "",
    "shortcut": "",
    "event": "",
    "load": "immediate",
}

ArgTuple = namedtuple("ArgTuple", ["name", "global_events", "local_events", "menus"])
ArgTuple.__new__.__defaults__ = (None,)
