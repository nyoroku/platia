from django import forms
from django.forms import inlineformset_factory
from .models import Property, Image, Message, County,Service, Category
from dal import autocomplete
ImageFormSet = inlineformset_factory(Property, Image, fields=['title', 'image'], extra=3, can_delete=True)


class UserLike(forms.Form):
    premise = forms.ModelChoiceField(queryset=Property.objects.all(), widget=forms.HiddenInput)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'phone', 'email', 'message')
        exclude = ('slug', 'premise', 'date')


class PropertyForm(forms.ModelForm):

    county = forms.ModelChoiceField(
        queryset=County.objects.all(),
        widget=autocomplete.ModelSelect2(url='premise:county-autocomplete')
    )

    class Meta:
        model = Property
        fields = ('price', 'county', 'type', 'bathrooms', 'bedrooms', 'name', 'amenities', 'purpose', 'details', 'key_features',
              'slug', 'tags', 'size', 'agent')


class ServiceForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Service
        fields = ('name', 'photo', 'county', 'ward', 'location', 'phone', 'price', 'tag_line', 'detail', 'categories'

                  )