import sys

from settings import logger
from components import resolve_path, load_config, load_package, load_version, query_files, build_package, build_rvpkg


def build(directory):
    directory = resolve_path(directory)
    config = load_config(directory)
    from pprint import pprint
    pprint(config)
    package = load_package()

    files = query_files(directory, config)
    version = load_version(config, files)

    package_text = build_package(package, config, files, version)
    return build_rvpkg(files, directory, version, config, package_text)


if __name__ == "__main__":
    final_package = build(sys.argv[-1])
    logger.info("Package successfully written to %s" % final_package)
