#coding = utf-8

# from django.template import Library
from django import template

register = template.Library()
@register.filter
def md(value):
    import markdown
    # from markdown import markdown
    return markdown.markdown(value)
