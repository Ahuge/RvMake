import sys

from settings import logger, INIT_FUNCTION_NAME
from components import resolve_path, load_config, load_package, load_version, query_files, build_package, build_rvpkg, \
    sort_init_call, query_init_call, get_driver


def build(directory):
    directory = resolve_path(directory)
    config = load_config(directory)
    from pprint import pprint
    pprint(config)
    package = load_package()

    files = query_files(directory, config)
    init_calls = query_init_call(config, files, INIT_FUNCTION_NAME)
    init_call = None
    if init_calls:
        init_call = init_calls[0]
    menus, shortcuts, events = sort_init_call(init_call)

    version = load_version(config, files)

    driver = get_driver(config['main'], files)
    package_text = build_package(package, config, files, version, driver, menus, shortcuts, events)
    return build_rvpkg(files, directory, version, config, package_text)


if __name__ == "__main__":
    final_package = build(sys.argv[-1])
    logger.info("Package successfully written to %s" % final_package)
