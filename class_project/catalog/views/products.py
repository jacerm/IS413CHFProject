from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django.contrib.auth import authenticate, login
from catalog import models as cmod
from account import models as amod
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, Group
import datetime

@permission_required('product.add_product', login_url='/homepage/index')
@view_function
def process_request(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/account/login')
        
    products = cmod.Product.objects.all()
    
    template_vars = {
        'products': products,
    }
    return dmp_render_to_response(request, 'products.html', template_vars)

@permission_required('product.add_product', login_url='/homepage/index')    
@view_function
def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('product_type') == 'Rental_Product':
                product = cmod.RentalProduct()
                product.name = form.cleaned_data.get('name')
                product.description = form.cleaned_data.get('description')
                product.image = form.cleaned_data.get('image')
                product.status = form.cleaned_data['status']
                
            elif form.cleaned_data.get('product_type') == 'Individual_Product':
                product = cmod.IndividualProduct()
                product.name = form.cleaned_data.get('name')
                product.description = form.cleaned_data.get('description')
                product.image = form.cleaned_data.get('image')
                product.creator = form.cleaned_data['creator']
                
            elif form.cleaned_data.get('product_type') == 'Bulk_Product':
                product = cmod.BulkProduct()
                product.name = form.cleaned_data.get('name')
                product.description = form.cleaned_data.get('description')
                product.image = form.cleaned_data.get('image')
                product.quantity = form.cleaned_data['quantity']
            
            product.save()
            return HttpResponseRedirect('/catalog/products/')
    
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'products.create.html', template_vars)
    
PRODUCT_CHOICES = (
    ("Rental_Product", "Rental Product"),
    ("Individual_Product", "Individual Product"),
    ("Bulk_Product", "Bulk Product"),
)

STATUS_CHOICES = (
    ("Available", "Available"),
    ("Unavailable", "Unavailable"),
)

STATUS_CHOICES_MAP = dict(STATUS_CHOICES)
    
class CreateForm(forms.Form): 
    
    name = forms.CharField(label='Product Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    description = forms.CharField(label='Description', required=True, max_length=10, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    image = forms.CharField(label='Image', required=True, max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    product_type = forms.ChoiceField(label="Product Type", required=False, choices=PRODUCT_CHOICES, widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    status = forms.ChoiceField(label="Status", required=False, choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    creator = forms.ModelChoiceField(label="Creator", required=False, queryset=amod.User.objects.order_by('first_name', 'last_name'), widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    quantity = forms.CharField(label="Quantity", required=False, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))

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

@permission_required('product.change_product', login_url='/homepage/index')   
@view_function
def edit(request):
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except amod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/products')
    
    form = EditForm(initial=model_to_dict(product))
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            if isinstance(product, cmod.RentalProduct):
                product.name = form.cleaned_data.get('name')
                product.description = form.cleaned_data.get('description')
                product.image = form.cleaned_data.get('image')
                product.status = form.cleaned_data['status']
                product.save()
                
            elif isinstance(product, cmod.IndividualProduct):
                product.name = form.cleaned_data.get('name')
                product.description = form.cleaned_data.get('description')
                product.image = form.cleaned_data.get('image')
                product.creator = form.cleaned_data['creator']
                product.save()
                
            else:
                product.name = form.cleaned_data.get('name')
                product.description = form.cleaned_data.get('description')
                product.image = form.cleaned_data.get('image')
                product.quantity = form.cleaned_data['quantity']
                product.save()
                
            return HttpResponseRedirect('/catalog/products/')
    
    template_vars = {
        'form': form,
        'product': product,
    }
    return dmp_render_to_response(request, 'products.edit.html', template_vars)
    
PRODUCT_CHOICES = (
    ("Rental_Product", "Rental Product"),
    ("Individual_Product", "Individual Product"),
    ("Bulk_Product", "Bulk Product"),
)

STATUS_CHOICES = (
    ("Available", "Available"),
    ("Unavailable", "Unavailable"),
)
    
class EditForm(forms.Form):
    name = forms.CharField(label='Product Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    description = forms.CharField(label='Description', required=True, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    image = forms.CharField(label='Image', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))
    status = forms.ChoiceField(label="Status", required=False, choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    creator = forms.ModelChoiceField(label="Creator", required=False, queryset=amod.User.objects.order_by('first_name', 'last_name'), widget=forms.Select(attrs={'class': 'form-control dropdown', 'style': 'margin-bottom: 15px;'}))
    quantity = forms.CharField(label="Quantity", required=False, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 15px;'}))

@permission_required('product.delete_product', login_url='/homepage/index')       
@view_function
def delete(request):
    try:
        product = cmod.Product.objects.get(id = request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect("/catalog/products")
        
    product.delete()
    
    return HttpResponseRedirect("/catalog/products")
    
@permission_required('product.add_product', login_url='/homepage/index')
@view_function
def getQuantity(request):
    try:
        product = cmod.Product.objects.get(id = request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect("/catalog/products")
    return HttpResponse(product.quantity)