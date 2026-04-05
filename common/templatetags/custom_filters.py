from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        return f"${float(value):,.0f}"
    except (ValueError, TypeError):
        return value