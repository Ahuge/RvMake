import ast
from .utils import get_driver


def walk_tree_for(tree, type_, attr_name):
    for node in ast.walk(tree):
        if isinstance(node, type_):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id == attr_name:
                        if isinstance(node.value, ast.Num):
                            return node.value.n
                        elif isinstance(node.value, ast.Str):
                            return node.value.s
                        else:
                            pass


def get_get_attr_value(config, files, function_name="__version__"):
    driver_path = get_driver(config['main'], files)
    tree = ast.parse(open(driver_path).read())
    result = walk_tree_for(tree, ast.Assign, function_name)
    return result


__all__ = ["get_get_attr_value"]
