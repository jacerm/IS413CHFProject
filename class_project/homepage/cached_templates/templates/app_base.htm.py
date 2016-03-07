# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457189576.1727197
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main', 'title', 'nav']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def nav():
            return render_nav(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <p>Test</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF</title>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container-fluid navbar navbar-default" style="margin-bottom: 0; padding-left: 0px; padding-right: 0px;">\r\n       <div class="row">\r\n          <div class="col-md-12">\r\n             <nav class="container" role="navigation">\r\n                <div class="navbar-header">\r\n                   <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                   <span class="sr-only">Toggle navigation</span>\r\n                   <span class="icon-bar"></span>\r\n                   <span class="icon-bar"></span>\r\n                   <span class="icon-bar"></span>\r\n                   </button>\r\n                   <a class="navbar-brand" href="/homepage/index""><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/chf.png" style="height: 26px;"></a>\r\n                </div>\r\n                <!-- Collect the nav links, forms, and other content for toggling -->\r\n                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                   <ul class="nav navbar-nav">\r\n')
        if request.user.is_superuser:
            __M_writer('                      <li id="users_tab"><a href="/manager/users">Manage Users</a></li>\r\n                      <li id="products_tab"><a href="/catalog/products">Manage Products</a></li>\r\n                      <li id="venues_tab"><a href="/event/venues">Manage Venues</a></li>\r\n                      <li id="events_tab"><a href="/event/events">Manage Events</a></li>\r\n')
        if not request.user.is_superuser:
            __M_writer('                      <li id="index_tab"><a href="/homepage/index">Home</a></li>\r\n                      <li id="about_tab"><a href="/homepage/about">About</a></li>\r\n                      <li id="contact_tab"><a href="/homepage/contact">Contact</a></li>\r\n                      <li id="terms_tab"><a href="/homepage/terms">Terms</a></li>\r\n                      <li id="faq_tab"><a href="/homepage/faq">FAQ</a></li>\r\n')
        __M_writer('                   </ul>\r\n                   <!--<form class="navbar-form navbar-left" role="search">\r\n                      <div class="form-group">\r\n                         <input type="text" class="form-control" placeholder="Search">\r\n                      </div>\r\n                      <button type="submit" class="btn btn-default">Submit</button>\r\n                   </form>-->\r\n                   <ul class="nav navbar-nav navbar-right">\r\n')
        if request.user.is_authenticated():
            __M_writer('                      <li><a>Welcome, ')
            __M_writer(str(request.user.first_name))
            __M_writer('</a></li>\r\n')
        __M_writer('                      <li class="dropdown">\r\n                         <a id="accountTab" href="#" class="dropdown-toggle" data-toggle="dropdown">Account<b class="caret"></b></a>\r\n                         <ul class="dropdown-menu" style="padding: 15px;min-width: 250px;">\r\n')
        if request.user.is_authenticated():
            __M_writer('                            <li><a href="/account/index">Account Information</a></li>\r\n                            <li><a href="/account/passchange">Change Password</a></li>\r\n')
        __M_writer('                            <li><a href="/account/signup">Register</a></li>\r\n                         </ul>\r\n                      </li>\r\n')
        if request.user.is_authenticated():
            __M_writer('                    <li><a href="/account/logout">Log Out</a></li>\r\n')
        else:
            __M_writer('                    <li><a id="loginButton" href="#myModal" data-toggle="modal">Log In</a></li>\r\n')
        __M_writer('                   </ul>\r\n                </div>\r\n             </nav>\r\n          </div>\r\n       </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"67": 71, "73": 3, "119": 113, "79": 3, "85": 7, "110": 59, "28": 0, "93": 7, "94": 19, "95": 19, "96": 24, "97": 25, "98": 30, "99": 31, "100": 37, "101": 45, "102": 46, "103": 46, "104": 46, "41": 1, "106": 51, "107": 52, "108": 55, "109": 58, "46": 5, "111": 60, "112": 61, "113": 63, "51": 69, "105": 48, "61": 71}, "filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/app_base.htm", "source_encoding": "utf-8", "uri": "app_base.htm"}
__M_END_METADATA
"""
