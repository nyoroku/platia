from django import template
from premise.models import Property


def do_top_shortstay(parser, token):
    return ShortStayNode()


class ShortStayNode(template.Node):
    def render(self, context):
        context['top_shortstay'] = Property.objects.filter(purpose__exact='short stay').order_by('sponsored')[:10]
        return ''


register = template.Library()
register.tag('get_top_shortstay', do_top_shortstay)




