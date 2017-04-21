from django import template
from django.template.base import  Node
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def my_tag(valual):
	return  valual*2

