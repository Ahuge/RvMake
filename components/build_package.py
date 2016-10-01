import os
from settings import DEFAULT_CONFIG


def build_package_str(config):
    if "package" in config:
        return config["package"]
    return ""


def build_author_str(config):
    if "author" in config and config['author']:
        return "\nauthor: " + config["author"]
    return ""


def build_organization_str(config):
    if "organization" in config and config['organization']:
        return "\norganization: " + config["organization"]
    return ""


def build_contact_str(config):
    if "contact" in config and config['contact']:
        return "\ncontact: " + config["contact"]
    return ""


def build_version_str(config):
    if "version" in config and config['version']:
        return config["version"]
    return ""


def build_url_str(config):
    if "url" in config and config['url']:
        return "\nurl: " + config["url"]
    return ""


def build_min_rv_version_str(config):
    if "min_rv_version" in config:
        return config["min_rv_version"]
    return ""


def build_requires_str(config):
    if "requires" in config and config['requires']:
        return "\nrequires: %s" % config["requires"]
    return ""


def build_icon_str(config):
    if "icon" in config and config["icon"]:
        return "\nicon: " + config["icon"]
    return ""


def build_imageio_str(config):
    if "imageio" in config:
        if isinstance(config["imageio"], list):
            io_str = "\n\t- ".join(config["imageio"])
        else:
            io_str = "\n\t- ".join(config["imageio"].split(""))
        if io_str:
            return "\nimageio:\n\t " + io_str
        else:
            return "\nimageio: []"
    return ""


def build_movieio_str(config):
    if "movieio" in config:
        if isinstance(config["movieio"], list):
            io_str = "\n\t- ".join(config["movieio"])
        else:
            io_str = "\n\t- ".join(config["movieio"].split(""))
        if io_str:
            return "\nmovieio:\n\t " + io_str
        else:
            return "\nmovieio: []"
    return ""


def build_hidden_str(config):
    if "hidden" in config:
        return "\nhidden: " + str(config["hidden"])
    return ""


def build_system_str(config):
    if "system" in config:
        return "\nsystem: " + str(config["system"])
    return ""


def build_optional_str(config):
    if "optional" in config:
        return "\noptional: " + str(config["optional"])
    return ""


def build_modes_str(driver, menus, shortcuts, events, load, icon, requires):
    mode_template = """\n\nmodes:
    - file: {driver}{menus}{shortcuts}{events}{load}{icon}
    """
    menu_template = "\n\tmenu: {menu}"
    shortcut_template = "\n\tshortcut: {shortcut}"
    event_template = "\n\tevent: {event}"
    # requires_template = "\n\trequires: {requires}"

    template_dictionary = {"driver": os.path.basename(driver)}
    if load:
        template_dictionary["load"] = "\n\tload: %s" % load
    else:
        template_dictionary["load"] = ""
    if icon:
        template_dictionary["icon"] = "\n\ticon: %s" % icon
    else:
        template_dictionary["icon"] = ""

    menu_str = ""
    for menu in menus:
        menu_str += (menu_template.format(menu=menu))

    shortcut_str = ""
    for shortcut in shortcuts:
        shortcut_str += (shortcut_template.format(shortcut=shortcut))

    event_str = ""
    for event in events:
        event_str += (event_template.format(event=event))
    # requires_str = ""
    # if requires:
    #     requires_str = requires_template.format(requires=requires)

    template_dictionary["menus"] = menu_str
    template_dictionary["shortcuts"] = shortcut_str
    template_dictionary["events"] = event_str
    # template_dictionary["requires"] = requires_str

    return mode_template.format(**template_dictionary)


def build_files_str(files):
    files_template = """\nfiles: {files}"""
    file_template = "\n\t- file: {f}"
    file_str = ""
    for f in files:
        file_str += file_template.format(f=os.path.basename(f))
    return files_template.format(files=file_str)


def build_description_str(config):
    if "description" in config:
        return config["description"]
    return ""


def build_package(package_template, config, file_list, version, driver, menus, shortcuts, events):
    # Update defaults with our config.
    DEFAULT_CONFIG.update(config)
    # Add our version.
    DEFAULT_CONFIG['version'] = version

    # Calculate files

    # Update with our "files" code

    DEFAULT_CONFIG["package"] = build_package_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["author"] = build_author_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["organization"] = build_organization_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["contact"] = build_contact_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["version"] = build_version_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["url"] = build_url_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["min_rv_version"] = build_min_rv_version_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["requires"] = build_requires_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["icon"] = build_icon_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["imageio"] = build_imageio_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["movieio"] = build_movieio_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["hidden"] = build_hidden_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["system"] = build_system_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["optional"] = build_optional_str(DEFAULT_CONFIG)
    DEFAULT_CONFIG["modes"] = build_modes_str(driver, menus, shortcuts, events, DEFAULT_CONFIG.get("load", ""),
                                              DEFAULT_CONFIG.get("icon", ""), config.get("requires"))
    DEFAULT_CONFIG["files"] = build_files_str(file_list)
    DEFAULT_CONFIG["description"] = build_description_str(DEFAULT_CONFIG)

    template = package_template.format(**DEFAULT_CONFIG)

    return template
