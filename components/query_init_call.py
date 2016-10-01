import ast
from collections import deque

from settings import ArgTuple
from .utils import get_driver


class FuncCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self._name = deque()

    @property
    def name(self):
        return '.'.join(self._name)

    @name.deleter
    def name(self):
        self._name.clear()

    def visit_Name(self, node):
        self._name.appendleft(node.id)

    def visit_Attribute(self, node):
        try:
            self._name.appendleft(node.attr)
            self._name.appendleft(node.value.id)
        except AttributeError:
            self.generic_visit(node)


def parse_args(args):
    arg_list = []
    for arg in args:
        if isinstance(arg, ast.Str):
            arg_list.append("%s" % arg.s)
        elif isinstance(arg, ast.Name):
            value = arg.id
            if value == "None":
                arg_list.append(None)
            else:
                arg_list.append(value)
        elif isinstance(arg, ast.Num):
            arg_list.append(arg.n)
        elif isinstance(arg, ast.List):
            arg_list.append(parse_args(arg.elts))
        elif isinstance(arg, ast.Tuple):
            arg_list.append(tuple(parse_args(arg.elts)))
        elif isinstance(arg, ast.Attribute):
            arg_list.append(str(arg.value.id) + "." + str(arg.attr))
        else:
            print(arg, type(arg))
    return arg_list


def get_func_calls(tree, function_name):
    instances_of_calling = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            callvisitor = FuncCallVisitor()
            callvisitor.visit(node.func)
            if callvisitor.name == function_name:
                args = parse_args(node.args)
                print(args)
                if len(args) == 3:
                    arg_tuple = ArgTuple(name=args[0], global_events=args[1], local_events=args[2])
                else:
                    arg_tuple = ArgTuple(name=args[0], global_events=args[1], local_events=args[2], menus=args[3])
                instances_of_calling.append(arg_tuple)
    return instances_of_calling


def get_function_called(config, files, function_name="self.init"):
    driver_path = get_driver(config['main'], files)
    tree = ast.parse(open(driver_path).read())
    result = get_func_calls(tree, function_name)
    return result


__all__ = ["get_function_called"]
