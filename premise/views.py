from django.shortcuts import render, get_object_or_404
from .models import Property, Profile, Type, Image, Liked, Bookmark, Message, County, Service, Category
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, When, Value, Case, PositiveSmallIntegerField
from .filters import PropertyFilter
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from .forms import ImageFormSet, MessageForm, PropertyForm, ServiceForm
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from finders.decorators import finder_required, profile_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django_ajax.decorators import ajax
from dal import autocomplete


def premise(request):
    return render(request, 'premise/index.html')


def all_premises(request, tag_slug=None):
    premises = Property.objects.all().order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises })


def flat(request, tag_slug=None):
    premises = Property.objects.filter(type='flat')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def condos(request, tag_slug=None):
    premises = Property.objects.filter(type='condo').order_by('sponsored')
    total_premises = premises.count()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def commercial(request, tag_slug=None):
    premises = Property.objects.filter(type='commercial').order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag,  'total_premises': total_premises})


def townhouse(request, tag_slug=None):
    premises = Property.objects.filter(type='townhouse').order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()

    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def multi_family(request, tag_slug=None):
    premises = Property.objects.filter(type='multifamily').order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def rents(request, tag_slug=None):
    premises = Property.objects.filter(purpose='rent').order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()

    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def buy(request, tag_slug=None):
    premises = Property.objects.filter(purpose='buy').order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 20)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def short_stay(request, tag_slug=None):
    premises = Property.objects.filter(purpose='short_stay').order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 20)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def property_detail(request, year, month, day, prop):
    prop = get_object_or_404(Property, slug=prop)
    image = Image.objects.filter(property=prop)
    prop_tag_ids = prop.tags.values_list('id', flat=True)
    similar_props = Property.objects.filter(tags__in=prop_tag_ids).exclude(id=prop.id)
    similar_props = similar_props.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')[:5]
    return render(request, 'premise/property_detail.html', {'prop': prop, 'image': image, 'similar_props': similar_props})


def platia(request):
    f = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render(request, 'premise/search.html', {'filter': f})


def search(request, tag_slug=None):
    f = PropertyFilter(request.GET, queryset=Property.objects.all())
    premises = f.qs
    total_premises = premises.count()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        f = premises.filter(tags__in=[tag])

    paginator = Paginator(f.qs, 3)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'filter': f, 'total_premises': total_premises})


@method_decorator([login_required, profile_required], name='dispatch')
class PropertyListView(ListView):
    model = Property
    template_name = 'premise/my_list.html'

    def get_queryset(self):
        qs = super(PropertyListView, self).get_queryset()
        return qs.filter(agent=self.request.user)


class AgentMixin(object):
    def get_queryset(self):
        qs = super(AgentMixin, self).get_queryset()
        return qs.filter(agent=self.request.user)


class AgentEditMixin(object):
    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super(AgentEditMixin, form).form_valid(form)


class AgentPropertyMixin(AgentMixin, LoginRequiredMixin):
    model = Property

    success_url = reverse_lazy('premise:my_list')


class AgentPropertyEditMixin(AgentPropertyMixin, AgentEditMixin):


    template_name = 'premise/form.html'


@method_decorator([login_required, profile_required], name='dispatch')
class ManagePropertyListView(AgentPropertyMixin, ListView):
    template_name = 'premise/my_list.html'
    model = Property
    context_object_name = 'premises'
    paginate_by = 15
    queryset = Property.objects.all()


@method_decorator([login_required, profile_required], name='dispatch')
class PropertyCreateView(SuccessMessageMixin, AgentPropertyMixin, CreateView, PermissionRequiredMixin):
    model = Property
    form_class = PropertyForm
    template_name = 'premise/form.html'
    success_message = '%(name)s Successfully Created'

    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super(PropertyCreateView, self).form_valid(form)


@method_decorator([login_required, profile_required], name='dispatch')
class PropertyUpdateView(SuccessMessageMixin, AgentPropertyMixin, UpdateView, PermissionRequiredMixin):

    template_name = 'premise/form.html'
    success_message = '%(name)s Successfully Updated'


@method_decorator([login_required, profile_required ], name='dispatch')
class PropertyDeleteView(SuccessMessageMixin, AgentPropertyMixin, DeleteView, PermissionRequiredMixin):
    template_name = 'premise/delete.html'
    success_url = reverse_lazy('premise:my_list')

    success_message = '%(name)s Successfully Deleted'


@method_decorator([login_required, profile_required], name='dispatch')
class PropertyImageUpdateView(TemplateResponseMixin, View):
    template_name = 'premise/formset.html'
    property = None

    def get_formset(self, data=None):
        return ImageFormSet(instance=self.property, data=data)

    def dispatch(self, request, pk):
        self.property = get_object_or_404(Property, id=pk, agent=request.user)
        return super(PropertyImageUpdateView, self).dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'property': self.property, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if request.method == 'POST':
            formset = ImageFormSet(request.POST, request.FILES, instance=self.property)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Image(s) for %(name)s  updated')
            return redirect('premise:my_list')
        else:
            messages.error(request, 'There was a problem updating image(s)')
        return self.render_to_response({'property': self.property, 'formset': formset})


def nicosia_rent(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='rent'), Q(district='nicosia')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def famagusta_rent(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='rent'), Q(district='famagusta')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def limassol_rent(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='rent'), Q(district='limassol')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def larnaca_rent(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='rent'), Q(district='larnaca')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises} )


def paphos_rent(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='rent'), Q(district='paphos')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def kyrenia_rent(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='rent'), Q(district='kyrenia')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def nicosia_buy(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='buy'), Q(district='nicosia')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def famagusta_buy(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='buy'), Q(district='famagusta')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def limassol_buy(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='buy'), Q(district='limassol')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def larnaca_buy(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='buy'), Q(district='larnaca')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def paphos_buy(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='buy'), Q(district='paphos')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def kyrenia_buy(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='buy'), Q(district='kyrenia')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def nicosia_short(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='short_stay'), Q(district='nicosia')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def famagusta_short(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='short_stay'), Q(district='famagusta')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def limassol_short(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='short_stay'), Q(district='limassol')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag, 'total_premises': total_premises})


def larnaca_short(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='short_stay'), Q(district='larnaca')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def paphos_short(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='short_stay'), Q(district='paphos')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


def kyrenia_short(request, tag_slug=None):
    premises = Property.objects.filter(Q(purpose='short_stay'), Q(district='kyrenia')).order_by('sponsored')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        premises = premises.filter(tags__in=[tag])
    total_premises = premises.count()
    paginator = Paginator(premises, 2)
    page = request.GET.get('page')
    try:
        premises = paginator.page(page)
    except PageNotAnInteger:
        premises = paginator.page(1)
    except EmptyPage:
        premises = paginator.page(paginator.num_pages)
    return render(request, 'premise/property.html', {'premises': premises, 'page': page, 'tag': tag , 'total_premises': total_premises})


@login_required()
def add_bookmark(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    bookmark = 0
    try:
        Bookmark.objects.get(user__pk=request.user.id, property__pk=property.id)
    except Bookmark.DoesNotExist:
        bookmark = Bookmark.objects.create(user=request.user, property=property)
    return HttpResponseRedirect(bookmark)


@method_decorator([login_required, ],name='dispatch')
class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'premise/saved.html'
    paginate_by = 20

    def get_queryset(self):
        qs = super(BookmarkListView, self).get_queryset()
        return qs.filter(user=self.request.user)


def about(request):
    return render(request, 'premise/aboutus.html')


def message_agent(request, premise_id):
    premise = get_object_or_404(Property, pk=premise_id)
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.premise = premise
            new_form.save()
            messages.success(request, 'Your message has been sent.The Agent will contact you')
            return HttpResponseRedirect(premise.get_absolute_url())
        else:
            messages.error(request, 'There has been an error sending your message')
    else:
        form = MessageForm()
    return render(request, 'premise/message.html', {'form': form, 'premise': premise})


def message_list(request):
    texts = Message.objects.filter(premise__agent=request.user)
    paginator = Paginator(texts, 5)
    page = request.GET.get('page')
    try:
        texts = paginator.page(page)
    except PageNotAnInteger:
        texts = paginator.page(1)
    except EmptyPage:
        texts = paginator.page(paginator.num_pages)

    return render(request, 'premise/message_list.html', {'texts': texts, 'page': page, })


def type_detail(request, type):
    type = get_object_or_404(Type, slug=type)
    premises = Property.objects.filter(property=type)
    return render(request, 'premise/type_html.html', {'type': type, 'premises': premises})


class CountyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = County.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs




@method_decorator([login_required, profile_required], name='dispatch')
class ServiceListView(ListView):
    model = Property
    template_name = 'premise/my_list.html'

    def get_queryset(self):
        qs = super(ServiceListView, self).get_queryset()
        return qs.filter(agent=self.request.user)


class WorkerMixin(object):
    def get_queryset(self):
        qs = super(WorkerMixin, self).get_queryset()
        return qs.filter(owner=self.request.user)


class WorkerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(WorkerEditMixin, form).form_valid(form)


class WorkerServiceMixin(WorkerMixin, LoginRequiredMixin):
    model = Service

    success_url = reverse_lazy('premise:my_services')


class WorkerServiceEditMixin(WorkerServiceMixin, WorkerEditMixin):


    template_name = 'premise/service.html'


@method_decorator([login_required, profile_required], name='dispatch')
class ManageServiceListView(WorkerServiceMixin, ListView):
    template_name = 'premise/my_services.html'
    model = Service
    context_object_name = 'services'
    paginate_by = 15
    queryset = Service.objects.all()


@method_decorator([login_required, profile_required], name='dispatch')
class ServiceCreateView(SuccessMessageMixin, WorkerServiceMixin, CreateView, PermissionRequiredMixin):
    model = Service
    form_class = ServiceForm
    template_name = 'premise/service.html'
    success_message = '%(name)s Successfully Created'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ServiceCreateView, self).form_valid(form)


@method_decorator([login_required, profile_required], name='dispatch')
class SericeUpdateView(SuccessMessageMixin, WorkerServiceMixin, UpdateView, PermissionRequiredMixin):

    template_name = 'premise/service.html'
    success_message = '%(name)s Successfully Updated'


@method_decorator([login_required, profile_required ], name='dispatch')
class ServiceDeleteView(SuccessMessageMixin, WorkerServiceMixin, DeleteView, PermissionRequiredMixin):
    template_name = 'premise/delete_service.html'
    success_url = reverse_lazy('premise:my_services')

    success_message = '%(name)s Successfully Deleted'


def category_detail(request, categories):
    categories = get_object_or_404(Category, slug=categories)
    services = Service.objects.filter(categories=categories)
    order = request.GET.get('order', 'name')
    services = services.order_by(order)

    total_services = services.count()
    paginator = Paginator(services, 24)
    page = request.GET.get('page')
    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)
    return render(request, 'premise/services_detail.html', {'order': order, 'services': services, 'page': page,
                                                      'total_services': total_services, 'category': categories})


@login_required
def dashboard(request):
    return render(request, 'premise/dashboard.html')



















