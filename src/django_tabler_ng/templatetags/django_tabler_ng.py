from math import floor
from urllib.parse import parse_qs, urlparse, urlunparse

from django import template
from django.contrib.messages import constants as message_constants
from django.template import Context
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

register = template.Library()

@register.inclusion_tag('django_tabler_ng/menu.html', takes_context=True)
def django_tabler_menu(context):
    return context