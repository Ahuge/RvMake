import os
import zipfile

from .exception_classes import PackagingException
from settings import logger
from .utils import resolve_path


def build_rvpkg(file_list, directory, version, config, package_text):
    package_name = '%s-%s.rvpkg' % (os.path.splitext(config['main'])[0], version)
    if "build path" not in config:
        raise PackagingException("No \"build path\" set in config. Please set \"build path\" to a folder on disk.")
    package_path = os.path.join(resolve_path(config["build path"]), package_name)

    if os.path.exists(package_path):
        logger.warning("Deleting %s" % package_path)
        os.remove(package_path)

    with zipfile.ZipFile(package_path, 'w') as zFile:
        for file_ in file_list:
            zFile.write(file_, file_.replace(directory, ""))
        zFile.writestr("PACKAGE", package_text)
    return package_path
