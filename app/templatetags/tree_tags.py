from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def generate_html_tree(objs):
    # html = '<ul>'
    html = ""
    for obj in objs:
        html += f'<li>{obj.title}</li>'
        if obj.children:
            html += generate_html_tree(obj.children.all())
        html += '</ul>'
    # html += '</ul>'

    return format_html(html)

