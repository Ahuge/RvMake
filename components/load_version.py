from .exception_classes import BuildException
from .query_version import get_get_attr_value


def load_version(config, files):
    result = get_get_attr_value(config, files, "__version__")
    print(result)
    if not result:
        raise BuildException("Could not parse version from config[\"main\"] file. Do you have a __version__ set?")
    return result
