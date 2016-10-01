from .exception_classes import ConfigurationException, BuildException
from .utils import import_driver


def load_version(config, files):
    if "main" not in config:
        raise ConfigurationException("Could not find \"main\" key in configuration file. "
                                     "This file should contain the entry point for your plugin.")

    possible_drivers = sorted(filter(lambda x: True if config['main'] in x else False, files),
                              key=lambda x: len(x))

    if not possible_drivers:
        raise ConfigurationException("Could not find a suitable %s in the list of gathered files:\n\t%s"
                                     % (config['main'], "\n\t".join(files)))

    module = import_driver(possible_drivers[0])
    if not hasattr(module, "__version__"):
        raise BuildException("Could not parse version from config[\"main\"] file. Do you have a __version__ set?")
    return module.__version__
