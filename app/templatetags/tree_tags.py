from django import template

register = template.Library()


# @register.simple_tag
# def generate_html_tree(objs):
#     html = '<ul>'
#     for obj in objs:
#         html += f'<li>{obj.title}</li>'
#         if obj.children:
#             html += generate_html_tree(obj.children.all())
#         # html += '</li>'
#     html += '</ul>'
#     return html


@register.simple_tag
def generate_html_tree(objs):
    html = '<ul class="nested">'
    objs = list(objs)
    for obj in objs:
        html += f'<li>{obj.title}</li>'
        objs.remove(obj)
        if obj.children:
            html += generate_html_tree(obj.children.all())
        html += '</li>'
    html += '</ul>'
    return html

