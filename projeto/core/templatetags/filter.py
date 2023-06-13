from django import template
from django.template.defaultfilters import stringfilter

from core.models import PRODUCT_TYPE, PRODUCT_VOL

register = template.Library()


@stringfilter
def convert_type(value):
    res = ''
    if value:
        try:
            status = dict(PRODUCT_TYPE)
            res = status[value]
        except:
            pass
    return res


register.filter('convert_type', convert_type)

@stringfilter
def convert_vol(value):
    res = ''
    if value:
        try:
            status = dict(PRODUCT_VOL) 
            res = status[value]
        except:
            pass
    return res


register.filter('convert_vol', convert_vol)