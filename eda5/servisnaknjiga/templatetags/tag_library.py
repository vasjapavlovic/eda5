import datetime

from django import template


register = template.Library()

@register.filter()
def to_int(value):
    return int(value)

@register.filter()
def to_msec(value):
    vrednost = int(value.strftime("%s")) * 1000
    return vrednost


@register.filter()
def count(value):

    vrednost = 0
    for obj in value:
        vrednost += 1

    return vrednost
