import os


def build_package(package_template, config, file_list, version):
    files_replace = ""
    for file_ in file_list:
        files_replace += """\n\t- file: %s""" % os.path.basename(file_)
    template = package_template.format(files=files_replace, version=version, **config)

    return template
