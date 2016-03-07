from django.conf import settings
from django_mako_plus.controller import view_function
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    form = SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            u = User()
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('firstName')
            u.last_name = form.cleaned_data.get('lastName')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/homepage/index/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'signup.html', template_vars)
    
class SignupForm(forms.Form):
    '''The signup form'''
    firstName = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    lastName = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    username = forms.CharField(label='Username', required=True, max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address1 = forms.CharField(label='Address 1', required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address2 = forms.CharField(label='Address 2', required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address2 = forms.CharField(label='Address 2', required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    
    #Validates username 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username)
        if len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username
        
    #Validates 2 or more model values on the form
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords do not match. Please try again.')
        return self.cleaned_data