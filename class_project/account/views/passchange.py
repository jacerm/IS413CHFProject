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

    form = ChangeForm()
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        form.user = request.user
        if form.is_valid():
            u = request.user
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            user = authenticate(username=u.username, password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/homepage/index/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'passchange.html', template_vars)
    
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