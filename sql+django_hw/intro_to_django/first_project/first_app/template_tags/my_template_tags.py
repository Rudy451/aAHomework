from django import template
import time

register = template.Library()

@register.simple_tag
def my_template_method(sq_ft):
  return f'This is {sq_ft} square feet!!!'

@register.simple_tag
def get_current_time(format_string):
  return time.strftime(format_string)
