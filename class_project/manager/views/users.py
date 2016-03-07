from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from django.forms.models import model_to_dict
from .. import dmp_render, dmp_render_to_response
from django.contrib.auth import authenticate, login
from account import models as amod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group
import datetime

@permission_required('user.add_user', login_url='/homepage/index')
@view_function
def process_request(request):
        
    users = amod.User.objects.all().order_by('-is_superuser', 'first_name', 'last_name')
    
    template_vars = {
        'users': users,
    }
    return dmp_render_to_response(request, 'users.html', template_vars)

@permission_required('user.add_user', login_url='/homepage/index')
@view_function
def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            u = amod.User()
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('firstName')
            u.last_name = form.cleaned_data.get('lastName')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.set_password(form.cleaned_data.get('password'))
            u.birthdate = form.cleaned_data.get('birthdate')
            u.phone = form.cleaned_data.get('phone')
            u.save()
            
            u.groups.clear()
            u.user_permissions.clear()
            for group in form.cleaned_data['groups']:
                u.groups.add(group)
            for permission in form.cleaned_data['permissions']:
                u.user_permissions.add(permission)
            u.save()
            return HttpResponseRedirect('/manager/users/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'users.create.html', template_vars)

class CreateForm(forms.Form): 
    firstName = forms.CharField(label='First Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    lastName = forms.CharField(label='Last Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    username = forms.CharField(label='Username', required=True, max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    password = forms.CharField(label='Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    password2 = forms.CharField(label='Confirm Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address1 = forms.CharField(label='Address 1', required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address2 = forms.CharField(label='Address 2', required=True, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    birthdate = forms.DateField(label="Birthday", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], widget=forms.TextInput(attrs={'id': 'datetimepicker1', 'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    phone = forms.CharField(label="Phone Number", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    groups = forms.ModelMultipleChoiceField(label="Groups", required=False, queryset=Group.objects.all(), widget = forms.CheckboxSelectMultiple)
    permissions = forms.ModelMultipleChoiceField(label="Permissions", required=False, queryset=Permission.objects.all(), widget = forms.CheckboxSelectMultiple)

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

@permission_required('user.change_user', login_url='/homepage/index')
@view_function
def edit(request):
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users')
    
    form = EditForm(initial=model_to_dict(user))
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.address1 = form.cleaned_data.get('address1')
            user.address2 = form.cleaned_data.get('address2')
            user.birthdate = form.cleaned_data.get('birthdate')
            user.phone = form.cleaned_data.get('phone')
            user.save()
            
            user.groups.clear()
            user.user_permissions.clear()
            for group in form.cleaned_data['groups']:
                user.groups.add(group)
            for permission in form.cleaned_data['permissions']:
                user.user_permissions.add(permission)
            
            return HttpResponseRedirect('/manager/users/')
    
    template_vars = {
        'form': form,
        'user': user,
    }
    return dmp_render_to_response(request, 'users.edit.html', template_vars)
    
class EditForm(forms.Form):
    first_name = forms.CharField(label="First Name", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    last_name = forms.CharField(label="Last Name", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    email = forms.EmailField(label="Email", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address1 = forms.CharField(label="Address 1", required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    address2 = forms.CharField(label="Address 2", required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    birthdate = forms.DateField(label="Birthday", input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False, widget=forms.TextInput(attrs={'id': 'datetimepicker2','class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    phone = forms.CharField(label="Phone Number", required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    groups = forms.ModelMultipleChoiceField(label="Groups", required=False, queryset=Group.objects.all(), widget = forms.CheckboxSelectMultiple)
    permissions = forms.ModelMultipleChoiceField(label="Permissions", required=False, queryset=Permission.objects.all(), widget = forms.CheckboxSelectMultiple)
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = amod.User.objects.filter(username=username)
        if username and len(users) > 0:
            raise forms.ValidationError('This username is already taken.')
        return username

@permission_required('user.delete_user', login_url='/homepage/index')
@view_function
def delete(request):
    try:
        user = amod.User.objects.get(id = request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect("/manager/users")
        
    user.delete()
    
    return HttpResponseRedirect("/manager/users")

@permission_required('user.change_user', login_url='/homepage/index')
@view_function
def passchange(request):
    try:
        user = amod.User.objects.get(id=request.urlparams[0])
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/manager/users')
        
    form = ChangeForm()
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        form.user = user
        if form.is_valid():
            u = user
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return HttpResponseRedirect('/manager/users/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'users.passchange.html', template_vars)

class ChangeForm(forms.Form):
    '''The login form'''
    currentpassword = forms.CharField(label='Current Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    password = forms.CharField(label= 'New Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    password2 = forms.CharField(label='Confirm New Password', required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    
    def clean_currentpassword(self):
        if not self.user.check_password(self.cleaned_data.get('currentpassword')):
            raise forms.ValidationError('Incorrect current password. Try again')
            
        return self.cleaned_data.get('currentpassword')
    
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Your new passwords do not match. Please try again.')
        return self.cleaned_data