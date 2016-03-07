from django.conf import settings
from django_mako_plus.controller import view_function
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/login')

    form = ChangeForm(initial={
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'address1': request.user.address1,
        'address2': request.user.address2,
        'birthdate': request.user.birthdate,
        'phone': request.user.phone,
    })
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid():
            u = request.user
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.birthdate = form.cleaned_data.get('birthdate')
            u.phone = form.cleaned_data.get('phone')
            u.save()
            return HttpResponseRedirect('/homepage/index/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'index.html', template_vars)
    
class ChangeForm(forms.Form):
    '''The login form'''
    first_name = forms.CharField(label="First Name", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    last_name = forms.CharField(label="Last Name", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    email = forms.EmailField(label="Email", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address1 = forms.CharField(label="Address 1", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address2 = forms.CharField(label="Address 2", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    birthdate = forms.DateField(label="Birthday", widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    phone = forms.CharField(label="Phone Number", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username)
        if len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username