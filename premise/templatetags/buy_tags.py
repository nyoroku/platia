from django import template
from premise.models import Property


def do_top_buys(parser, token):
    return BuyNode()


class BuyNode(template.Node):
    def render(self, context):
        context['top_buys'] = Property.objects.filter(purpose__exact='buy').order_by('sponsored')[:10]
        return ''


register = template.Library()
register.tag('get_top_buys', do_top_buys)




