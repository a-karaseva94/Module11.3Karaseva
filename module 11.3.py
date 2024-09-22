import inspect
from pprint import pprint


def introspection_info(obj):
    info_about_object = {}
    info_about_object['Тип объекта'] = type(obj).__name__
    info_about_object['Атрибуты объекта'] = obj.__dict__
    info_about_object['Методы и атрибуты объекта'] = dir(obj)
    info_about_object['Модуль, к которому принадлежит объект'] = inspect.getmodule(obj)
    info_about_object['Есть ли атрибут name у объекта'] = hasattr(obj, 'name')
    info_about_object['Объект вызываемый?'] = callable(obj)
    return info_about_object


class ClassInfo:
    def __init__(self):
        self.name = 'Nick'
        self.years = 22


obj = ClassInfo()
number_info = introspection_info(obj)
pprint(number_info)
