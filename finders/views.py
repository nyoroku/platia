from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from premise.models import Profile
from django.shortcuts import render, redirect
from .forms import ProfileEditForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from premise.models import User
from .forms import FinderRegistrationForm, AgentRegistrationForm
from .decorators import finder_required, profile_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


class FinderRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'finders/register.html'
    form_class = FinderRegistrationForm
    success_url = reverse_lazy('index')
    success_message = 'Account Successfully Created.Welcome %(username)%'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'finder'
        return super(FinderRegistrationView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        result = super(FinderRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'],


                            )

        login(self.request, user)
        return result


class AgentRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'finders/registration.html'
    form_class = AgentRegistrationForm
    success_url = reverse_lazy('premise:dashboard')
    success_message = 'Thank You %(username)s for joining our team.Please complete your profile detail'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'finder'
        return super(AgentRegistrationView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()
        user.profile.company = form.cleaned_data.get('company')
        user.profile.number = form.cleaned_data.get('number')
        user.save()
        result = super(AgentRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'],)

        login(self.request, user)

        return result
    



@profile_required
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated')
            return redirect('finders:profile')
        else:
            messages.error(request, 'There was a problem when updating profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'finders/edit.html', {'user_form': user_form, 'profile_form': profile_form})

def profile(request):
    proname = Profile.objects.filter(user=request.user)
    return render(request, 'finders/profile.html', {'section': 'profile', 'proname': proname})


def common_view(request):
    user = request.user
    if user.is_finder:
        return redirect('index')

    else:
        return redirect('premise:my_list')
