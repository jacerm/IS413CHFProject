# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453393402.838508
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main', 'content_head', 'right_aside', 'nav_links', 'left_aside']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def main():
            return render_main(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        password = context.get('password', UNDEFINED)
        email = context.get('email', UNDEFINED)
        def nav_links():
            return render_nav_links(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        message = context.get('message', UNDEFINED)
        def content_head():
            return render_content_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_links'):
            context['self'].nav_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_head'):
            context['self'].content_head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_aside'):
            context['self'].left_aside(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_aside'):
            context['self'].right_aside(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        message = context.get('message', UNDEFINED)
        email = context.get('email', UNDEFINED)
        password = context.get('password', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-sm-12 center_divider">\r\n        <h3>Add Your Suggestions</h3>\r\n        <form role="form" method="POST">\r\n            <div class="form-group">\r\n                <label for="email">Email address:</label>\r\n                <input type="email" name="youremail" class="form-control" placeholder="Enter Email" id="email" style="width: 50%;">\r\n            </div>\r\n            <div class="form-group">\r\n                <label for="pwd">Password:</label>\r\n                <input type="password" name="yourpassword" class="form-control" placeholder="Enter Password" id="pwd" style="width: 50%;">\r\n            </div>\r\n            <div class="form-group">\r\n                <label for="msg">Message:</label>\r\n                <textarea type="text" name="yourmessage" class="form-control" placeholder="Enter Message" id="pwd" style="width: 50%;"></textarea>\r\n            </div>\r\n            <button type="submit" class="btn btn-default">Submit</button>\r\n        </form>\r\n')
        if email:
            __M_writer('        <h3>Your Post Submission</h3>\r\n        <p>')
            __M_writer(str( email ))
            __M_writer('</p>\r\n')
        if password:
            __M_writer('        <p>')
            __M_writer(str( password ))
            __M_writer('</p>\r\n')
        if message:
            __M_writer('        <p>')
            __M_writer(str( message ))
            __M_writer('</p>\r\n')
        __M_writer('    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Contact Page</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_aside(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_aside():
            return render_right_aside(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav_links():
            return render_nav_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li id="index_tab"><a href="/homepage/index">Home</a></li>\r\n    <li id="about_tab"><a href="/homepage/about">About</a></li>\r\n    <li id="contact_tab"><a href="/homepage/contact">Contact</a></li>\r\n    <li id="terms_tab"><a href="/homepage/terms">Terms</a></li>\r\n    <li id="faq_tab"><a href="/homepage/faq">FAQ</a></li>\r\n    <li id="sections_tab"><a href="/homepage/sections">Sections</a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_aside(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_aside():
            return render_left_aside(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "contact.html", "source_encoding": "utf-8", "filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/contact.html", "line_map": {"128": 3, "66": 50, "134": 3, "140": 18, "76": 21, "152": 146, "146": 18, "85": 21, "86": 39, "87": 40, "88": 41, "89": 41, "90": 43, "91": 44, "92": 44, "93": 44, "94": 46, "95": 47, "96": 47, "97": 47, "98": 49, "104": 12, "28": 0, "110": 12, "46": 1, "51": 10, "116": 52, "56": 16, "122": 52, "61": 19}}
__M_END_METADATA
"""
