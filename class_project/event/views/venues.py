from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django.contrib.auth import authenticate, login
from event import models as emod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group
import datetime

@permission_required('venue.add_venue', login_url='/homepage/index')
@view_function
def process_request(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/account/login')
        
    venues = emod.Venue.objects.all()
    
    template_vars = {
        'venues': venues,
    }
    return dmp_render_to_response(request, 'venues.html', template_vars)
  
@permission_required('venue.add_venue', login_url='/homepage/index')  
@view_function
def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            v = emod.Venue()
            v.name = form.cleaned_data.get('name')
            v.address = form.cleaned_data.get('address')
            v.city = form.cleaned_data.get('city')
            v.state = form.cleaned_data.get('state')
            v.zip = form.cleaned_data.get('zip')
            v.save()
            return HttpResponseRedirect('/event/venues/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'venues.create.html', template_vars)
    
class CreateForm(forms.Form): 
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    city = forms.CharField(label='City', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    state = forms.CharField(label="State", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    zip = forms.CharField(label="Zip", required=True, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))

    #Validates username 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = amod.User.objects.filter(username=username)
        if len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username
        
        #Validates 2 or more model values on the form
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your passwords do not match. Please try again.')
        return self.cleaned_data

@permission_required('venue.delete_venue', login_url='/homepage/index')   
@view_function
def delete(request):
    try:
        venue = emod.Venue.objects.get(id = request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect("/event/venues")
        
    venue.delete()
    
    return HttpResponseRedirect("/event/venues")

@permission_required('venue.change_venue', login_url='/homepage/index')
@view_function
def edit(request):
    try:
        venue = emod.Venue.objects.get(id=request.urlparams[0])
    except emod.Venue.DoesNotExist:
        return HttpResponseRedirect('/event/venues')
    
    form = EditForm(initial=model_to_dict(venue))
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            venue.name = form.cleaned_data.get('name')
            venue.address = form.cleaned_data.get('address')
            venue.city = form.cleaned_data.get('city')
            venue.state = form.cleaned_data.get('state')
            venue.zip = form.cleaned_data.get('zip')
            venue.save()
            return HttpResponseRedirect('/event/venues')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'venues.edit.html', template_vars)
    
class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address = forms.CharField(label='Address', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    city = forms.CharField(label='City', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    state = forms.CharField(label="State", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    zip = forms.CharField(label="Zip", required=True, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = amod.User.objects.filter(username=username)
        if username and len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username