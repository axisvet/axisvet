from django import template

register = template.Library()


@register.filter(is_safe=True)
def settings_value(o, attr):
        return getattr(o, attr)
