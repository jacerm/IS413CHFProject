from django.conf import settings
from django_mako_plus.controller import view_function
from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponse('''
            <script>
                window.location.href = '/homepage/index'
            </script>
            ''')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'login.html', template_vars)
    
class LoginForm(forms.Form):
    '''The login form'''
    username = forms.CharField(label="Username", required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px; margin-left: 15px;'}))
    password = forms.CharField(label="Password", required=True, max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px; margin-left: 15px;'}))
    
    # #Validates username 
    # def clean_username(self):
    #     if User.objects.get(username=self.cleaned_data.get('username'))
    
    #Validates 2 or more model values on the form
    def clean(self):
        user = User
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError('This username and password does not match our records.')
        return self.cleaned_data