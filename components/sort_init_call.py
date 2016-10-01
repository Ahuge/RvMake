from settings import EVENT_KEY_STR
from yield_menu_items import yield_menu_items


def sort_init_call(init_call):
    all_events = []
    events = []
    shortcuts = []
    menus = []
    if init_call:
        if init_call.global_events:
            all_events.extend([name for name, func, title in init_call.global_events])
        if init_call.local_events:
            all_events.extend([key for key, func, title in init_call.local_events])

        for event in all_events:
            if event.startswith(EVENT_KEY_STR):
                shortcuts.append(event)
            else:
                events.append(event)

        if init_call.menus:
            for root_level_menu_tuple in init_call.menus:
                for menu_item in yield_menu_items(root_level_menu_tuple):
                    menus.append(menu_item)
    return menus, shortcuts, events