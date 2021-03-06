from django.conf import settings
from django_mako_plus.controller import view_function
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_response
from account.models import User

@view_function
def process_request(request):
    logout(request)
    return(HttpResponseRedirect('/homepage/index'))