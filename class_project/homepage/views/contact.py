from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):
    print('>>>>>>Email post: ', request.POST.get('youremail'))
    print('>>>>>>Password post: ', request.POST.get('yourpassword'))
    print('>>>>>>Message post: ', request.POST.get('yourmessage'))
    
    template_vars = {
        'email': request.POST.get('youremail'),
        'password': request.POST.get('yourpassword'),
        'message': request.POST.get('yourmessage'),
    }
    return dmp_render_to_response(request, 'contact.html', template_vars)