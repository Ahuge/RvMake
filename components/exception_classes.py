class BuildException(Exception):
    pass


class ConfigurationException(BuildException):
    pass


class PackagingException(BuildException):
    pass
