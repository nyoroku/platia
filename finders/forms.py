from django import forms
from premise.models import Profile
from django.contrib.auth.models import User
from premise.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture', 'company', 'logo', 'number', 'description')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class FinderRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=80, help_text='Required. Use avalid email', label='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password2', 'password1', 'username')

    def save(self, commit=True):
        user = super(FinderRegistrationForm, self).save(commit=False)
        user.is_finder = True
        if commit:
            user.save()
        return user


class AgentRegistrationForm(UserCreationForm):
    company = forms.CharField(max_length=50)
    number = PhoneNumberField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=80, help_text='Required. Use a valid Email', label='Email')
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'company', 'number', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super(AgentRegistrationForm, self).save(commit=False)
        user.is_profile = True
        if commit:
            user.save()
        return user

