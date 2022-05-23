from atexit import register
from os import curdir
from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all the values of "arg" from the string value
    """
    return value.replace(arg,'')

#register.filter('cut',cut)