from django import template

register = template.Library()

@register.filter()
def to_int(value):
    return int(value)


@register.filter()
def to_msec(value):
    vrednost = value*year*365 + value*month*12+value*hours*24*60*3600*1000
    return vrednost
