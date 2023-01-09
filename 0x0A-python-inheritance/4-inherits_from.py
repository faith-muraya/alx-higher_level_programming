#!/usr/bin/python3
''' module: 2-is_same_class
'''


def is_kind_of_class(obj, a_class):
    '''the object is an instance of a class that inherited (directly or indirectly)
    obj: an object
    a_class: a class
    returns None
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
