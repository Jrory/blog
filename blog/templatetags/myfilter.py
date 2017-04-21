# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.filter(name="month_to_upper")
def first_up(key):
	return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month - 1]


# @register.simple_tag()
@register.assignment_tag()
def my_upper(key):
	return key.upper()
