from django import template
from premise.models import Property


def do_top_rents(parser, token):
    return RentNode()


class RentNode(template.Node):
    def render(self, context):
        context['top_rents'] = Property.objects.filter(purpose__exact='rent').order_by('sponsored')[:10]
        return ''


register = template.Library()
register.tag('get_top_rents', do_top_rents)




