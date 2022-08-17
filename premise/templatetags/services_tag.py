from django import template
from premise.models import Category
from django.db.models import Q

def do_category(parser, token):
    return CategoryNode()


class CategoryNode(template.Node):
    def render(self, context):
        context['categories'] = Category.objects.all()[:9]
        return ''


register = template.Library()
register.tag('get_category', do_category)
