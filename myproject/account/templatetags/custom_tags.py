from datetime import datetime
from django import template

register = template.Library()


@register.filter(name='check')
def check(value:str, arg:str):
    y,m,d = arg.split('-')
    return value.upper() + " 오늘은 " + y + "년 " + m + "월 "+ d + "일입니다."


@register.simple_tag
def current_datetime(format_string):
    """Returns the current date and time formatted as per the given format string."""
    return datetime.now().strftime(format_string)


