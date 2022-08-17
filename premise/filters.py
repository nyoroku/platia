from .models import Property
import django_filters
from .models import County
from dal import autocomplete


class PropertyFilter(django_filters.FilterSet):
    TYPE = (
        ('flat', 'FLAT'),
        ('townhouse', 'TOWNHOUSE'),
        ('farm', 'FARM'),
        ('condo', 'CONDO'),
        ('commercial', 'COMMERCIAL'),
        ('land', 'LAND')
    )

    PURPOSE = (
        ('buy', 'BUY'),
        ('rent', 'RENT'),
        ('short stay', 'SHORT STAY'))

    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min. Price')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max. Price')
    county = django_filters.ModelChoiceFilter(name='county', queryset=County.objects.all(),
                                              widget=autocomplete.ModelSelect2(url='premise:county-autocomplete'))
    bathrooms = django_filters.NumberFilter(field_name='bathrooms')
    bedrooms = django_filters.NumberFilter(field_name='bedrooms')
    purpose = django_filters.ChoiceFilter(field_name='purpose', choices=PURPOSE, label='For')


    class Meta:
        model = Property
        fields = ['county', 'purpose', 'type', 'price', 'bedrooms', 'bathrooms']







