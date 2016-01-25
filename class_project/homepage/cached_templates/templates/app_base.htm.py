# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453306306.752125
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['nav', 'title', 'nav_links']


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
        def nav():
            return render_nav(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def nav_links():
            return render_nav_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def nav():
            return render_nav(context)
        def nav_links():
            return render_nav_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container-fluid navbar navbar-default" style="margin-bottom: 0; padding-left: 0px; padding-right: 0px;">\r\n       <div class="row">\r\n          <div class="col-md-12">\r\n             <nav class="container" role="navigation">\r\n                <div class="navbar-header">\r\n                   <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n                   <span class="sr-only">Toggle navigation</span>\r\n                   <span class="icon-bar"></span>\r\n                   <span class="icon-bar"></span>\r\n                   <span class="icon-bar"></span>\r\n                   </button>\r\n                   <a class="navbar-brand" href="/homepage/index""><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/chf.png" style="height: 26px;"></a>\r\n                </div>\r\n                <!-- Collect the nav links, forms, and other content for toggling -->\r\n                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                   <ul class="nav navbar-nav">\r\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_links'):
            context['self'].nav_links(**pageargs)
        

        __M_writer('\r\n                   </ul>\r\n                   <!--<form class="navbar-form navbar-left" role="search">\r\n                      <div class="form-group">\r\n                         <input type="text" class="form-control" placeholder="Search">\r\n                      </div>\r\n                      <button type="submit" class="btn btn-default">Submit</button>\r\n                   </form>-->\r\n                   <ul class="nav navbar-nav navbar-right">\r\n                      <li class="dropdown">\r\n                         <a href="#" class="dropdown-toggle" data-toggle="dropdown">Welcome, Jace <b class="caret"></b></a>\r\n                         <ul class="dropdown-menu" style="padding: 15px;min-width: 250px;">\r\n                            <li>\r\n                               <div class="row">\r\n                                  <div class="col-md-12">\r\n                                     <form class="form" role="form" method="post" action="login" accept-charset="UTF-8" id="login-nav">\r\n                                        <div class="form-group">\r\n                                           <label class="sr-only" for="exampleInputEmail2">Email address</label>\r\n                                           <input type="email" class="form-control" id="exampleInputEmail2" placeholder="Email address" required>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                           <label class="sr-only" for="exampleInputPassword2">Password</label>\r\n                                           <input type="password" class="form-control" id="exampleInputPassword2" placeholder="Password" required>\r\n                                        </div>\r\n                                        <div class="checkbox">\r\n                                           <label>\r\n                                           <input type="checkbox"> Remember me\r\n                                           </label>\r\n                                        </div>\r\n                                        <div class="form-group">\r\n                                           <button type="submit" class="btn btn-success btn-block">Sign in</button>\r\n                                        </div>\r\n                                     </form>\r\n                                  </div>\r\n                               </div>\r\n                            </li>\r\n                            <li class="divider"></li>\r\n                            <li>\r\n                               <input class="btn btn-primary btn-block" type="button" id="sign-in-google" value="Sign In with Google">\r\n                               <input class="btn btn-primary btn-block" type="button" id="sign-in-twitter" value="Sign In with Twitter">\r\n                            </li>\r\n                         </ul>\r\n                      </li>\r\n                      <li><a href="#">Log Out</a></li>\r\n                   </ul>\r\n                </div>\r\n             </nav>\r\n          </div>\r\n       </div>\r\n    </div>\r\n')
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


def render_nav_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav_links():
            return render_nav_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        Nav links go here with active classes\r\n                      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 7, "65": 19, "66": 19, "101": 95, "71": 26, "40": 1, "45": 5, "77": 3, "83": 3, "55": 7, "89": 24, "28": 0, "95": 24}, "filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/app_base.htm", "uri": "app_base.htm"}
__M_END_METADATA
"""
