def yield_menu_items(menu_tuple, root_name=""):
    if menu_tuple and len(menu_tuple) > 1:
        if isinstance(menu_tuple[0], str):
            names = yield_menu_items(menu_tuple=menu_tuple[1], root_name=menu_tuple[0])
            for name in names:
                if root_name:
                    yield root_name + "/" + name
                    yield name
        elif isinstance(menu_tuple[0], (tuple, list)):
            for menu_command in menu_tuple:
                if root_name:
                    yield root_name + "/" + menu_command[0]
                else:
                    yield menu_command[0]
