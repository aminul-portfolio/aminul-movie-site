from django import template

register = template.Library()

@register.filter
def split_by_comma(value):
    return value.split(',')

@register.filter
def split_by_comma(value):
    return [x.strip() for x in value.split(',')] if value else []
