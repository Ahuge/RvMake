import os
from third_party import yaml
from .exception_classes import BuildException, ConfigurationException
from settings import ACCEPTABLE_CONFIG_EXTENSIONS, logger
from .utils import resolve_path


def load_config(search_directory):
    search_directory = resolve_path(search_directory)
    files = os.listdir(search_directory)
    if not files:
        raise BuildException("No files found in %s, exiting..." % search_directory)

    config_files = [f for f in files if os.path.splitext(f)[1] in ACCEPTABLE_CONFIG_EXTENSIONS]
    if not config_files:
        raise BuildException("No config files found in %s, exiting..." % search_directory)

    config_file = None
    if len(config_files) > 1:
        for optional_config_file in config_files:
            if os.path.basename(search_directory) == os.path.splitext(optional_config_file)[0]:
                config_file = optional_config_file
    else:
        config_file = config_files[0]

    logger.info("Found config file %s" % os.path.join(search_directory, config_file))
    try:
        with open(os.path.join(search_directory, config_file), "rb") as fh:
            config_settings = yaml.load(fh)
    except yaml.YAMLError as e:
        raise ConfigurationException(str(e))

    return config_settings
