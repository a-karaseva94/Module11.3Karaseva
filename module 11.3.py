import inspect
from pprint import pprint


def introspection_info(obj):
    info_about_obj = {'Тип объекта': type(obj),
                      'Атрибуты объекта': [attr for attr in dir(obj) if
                                           not callable(getattr(obj, attr)) and not attr.startswith("__")],
                      'Магические атрибуты объекта': [attr for attr in dir(obj) if
                                           not callable(getattr(obj, attr)) and attr.startswith("__")],
                      'Методы объекта': [method for method in dir(obj) if
                                         callable(getattr(obj, method)) and not method.startswith("__")],
                      'Магические методы объекта': [method for method in dir(obj) if
                                                    callable(getattr(obj, method)) and method.startswith("__")],
                      'Модуль, к которому принадлежит объект': inspect.getmodule(obj),
                      'Есть ли атрибут name у объекта': hasattr(obj, 'name'),
                      'Объект вызываемый?': callable(obj)}
    return info_about_obj


number_info = introspection_info(42)
pprint(number_info)
