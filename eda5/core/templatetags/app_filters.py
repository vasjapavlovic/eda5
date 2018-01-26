from django import template

register = template.Library()



@register.filter(name='range_to_list')
def range_to_list(my_range):
    return list(my_range)
