import os

from settings import logger, INCLUDED_FILE_TYPE, PYTHON_INIT
from .utils import resolve_path


def query_files(directory, config):
    directory = resolve_path(directory)
    logger.debug("Querying for files in %s" % directory)
    all_files = os.listdir(directory)
    if "include types" not in config:
        config["include types"] = INCLUDED_FILE_TYPE

    files = []
    for file_ in all_files:
        file_path = os.path.join(directory, file_).replace("\\", "/")
        if os.path.isdir(file_path) and PYTHON_INIT in os.listdir(file_path):
            files.extend(query_files(file_path, config))
        elif os.path.isfile(file_path):
            if os.path.splitext(file_path)[1] in config["include types"]:
                logger.debug("Appending %s" % file_path)
                files.append(file_path)
    return files
