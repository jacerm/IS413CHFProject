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

@permission_required('event.add_event', login_url='/homepage/index')
@view_function
def process_request(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/account/login')
        
    events = emod.Event.objects.all()
    
    template_vars = {
        'events': events,
    }
    return dmp_render_to_response(request, 'events.html', template_vars)

@permission_required('event.add_event', login_url='/homepage/index')
@view_function
def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            e = emod.Event()
            e.name = form.cleaned_data.get('name')
            e.description = form.cleaned_data.get('description')
            e.start_date = form.cleaned_data.get('start_date')
            e.end_date = form.cleaned_data.get('end_date')
            e.venue = form.cleaned_data.get('venue')
            e.save()
            return HttpResponseRedirect('/event/events/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'events.create.html', template_vars)
    
class CreateForm(forms.Form): 
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    start_date = forms.DateField(label="Start Date", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False, widget=forms.TextInput(attrs={'id': 'datetimepicker3','class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    end_date = forms.DateField(label="End Date", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False, widget=forms.TextInput(attrs={'id': 'datetimepicker4','class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    venue = forms.ModelChoiceField(label="Venue", required=True, queryset=emod.Venue.objects.order_by("name"), widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))

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

@permission_required('event.delete_event', login_url='/homepage/index')
@view_function
def delete(request):
    try:
        event = emod.Event.objects.get(id = request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect("/event/events")
        
    event.delete()
    
    return HttpResponseRedirect("/event/events")

@permission_required('event.change_event', login_url='/homepage/index')
@view_function
def edit(request):
    try:
        event = emod.Event.objects.get(id=request.urlparams[0])
    except emod.Event.DoesNotExist:
        return HttpResponseRedirect('/event/events')
    
    areas = emod.Area.objects.filter(event_id = request.urlparams[0])
    
    form = EditForm(initial=model_to_dict(event))
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            event.name = form.cleaned_data.get('name')
            event.description = form.cleaned_data.get('description')
            event.start_date = form.cleaned_data.get('start_date')
            event.end_date = form.cleaned_data.get('end_date')
            event.venue = form.cleaned_data.get('venue')
            event.save()
            return HttpResponseRedirect('/event/events')
    
    template_vars = {
        'form': form,
        'areas': areas,
    }
    return dmp_render_to_response(request, 'events.edit.html', template_vars)
    
class EditForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    start_date = forms.DateField(label="Start Date", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False, widget=forms.TextInput(attrs={'id': 'datetimepicker5','class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    end_date = forms.DateField(label="End Date", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False, widget=forms.TextInput(attrs={'id': 'datetimepicker6','class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    venue = forms.ModelChoiceField(label="Venue", required=True, queryset=emod.Venue.objects.order_by("name"), widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = amod.User.objects.filter(username=username)
        if username and len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username
        
@permission_required('area.add_area', login_url='/homepage/index')
@view_function
def createarea(request):
    form = CreateAreaForm()
    if request.method == 'POST':
        form = CreateAreaForm(request.POST)
        if form.is_valid():
            a = emod.Area()
            a.name = form.cleaned_data.get('name')
            a.description = form.cleaned_data.get('description')
            a.place_number = form.cleaned_data.get('place_number')
            a.event = form.cleaned_data.get('event')
            a.save()
            return HttpResponseRedirect('/event/events.edit/{id}'.format(id=a.event.id))
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'events.createarea.html', template_vars)
    
class CreateAreaForm(forms.Form): 
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    place_number = forms.IntegerField(label='Place Number', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    event = forms.ModelChoiceField(label="Event", required=True, queryset=emod.Event.objects.order_by("name"), widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))

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
    
@permission_required('area.delete_area', login_url='/homepage/index')
@view_function
def areadelete(request):
    try:
        area = emod.Area.objects.get(id = request.urlparams[0])
    except emod.Area.DoesNotExist:
        return HttpResponseRedirect("/event/events.edit/{id}".format(id=area.event_id))
    area.delete()
    
    return HttpResponseRedirect("/event/events.edit/{id}".format(id=area.event_id))
    
@permission_required('area.change_area', login_url='/homepage/index')
@view_function
def editarea(request):
    try:
        area = emod.Area.objects.get(id=request.urlparams[0])
    except emod.Area.DoesNotExist:
        return HttpResponseRedirect('/event/events.edit/{id}'.format(id=area.event_id))
    
    form = EditAreaForm(initial=model_to_dict(area))
    if request.method == 'POST':
        form = EditAreaForm(request.POST)
        if form.is_valid():
            area.name = form.cleaned_data.get('name')
            area.description = form.cleaned_data.get('description')
            area.place_number = form.cleaned_data.get('place_number')
            area.event = form.cleaned_data.get('event')
            area.save()
            return HttpResponseRedirect('/event/events.edit/{id}'.format(id=area.event_id))
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'events.editarea.html', template_vars)
    
class EditAreaForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    place_number = forms.IntegerField(label='Place Number', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    event = forms.ModelChoiceField(label="Event", required=True, queryset=emod.Event.objects.order_by("name"), widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = amod.User.objects.filter(username=username)
        if username and len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username