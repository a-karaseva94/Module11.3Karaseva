import inspect
from pprint import pprint


def introspection_info(obj):
    info_about_object = {}
    info_about_object['Тип объекта'] = type(obj)
    info_about_object['Абрибуты и методы объекта'] = dir(obj)
    info_about_object['Модуль, к которому принадлежит объект'] = inspect.getmodule(obj)
    info_about_object['Есть ли атрибут NUMERATOR у объекта'] = hasattr(obj, 'numerator')
    info_about_object['Объект вызываемый?'] = callable(obj)
    return info_about_object


number_info_1 = introspection_info(42)
number_info_2 = introspection_info(introspection_info)
pprint(number_info_1)
pprint(number_info_2)