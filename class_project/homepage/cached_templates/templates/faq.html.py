# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453483703.3408597
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/faq.html'
_template_uri = 'faq.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main', 'nav_links', 'left_aside', 'content_head', 'right_aside']


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
        def nav_links():
            return render_nav_links(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
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
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-sm-12 center_divider">\r\n        <h3>Questions</h3>\r\n        <p>When was Colonial Heritage Foundation founded?</p>\r\n        <ul>\r\n            <li>It was founded in 1996</li>\r\n        </ul>\r\n        <p>When is the next Colonial Heritage Foundation event?</p>\r\n        <ul>\r\n            <li>This Saturday 1/23/16 at 10am.</li>\r\n        </ul>\r\n        <p>Who is the founder of the Colonial Heritage foundation?</p>\r\n        <ul>\r\n            <li>The founder is Gove Allen...I think</li>\r\n        </ul>\r\n    </div>\r\n')
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


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>FAQ Page</h3>\r\n    </div>\r\n')
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


"""
__M_BEGIN_METADATA
{"uri": "faq.html", "filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/faq.html", "line_map": {"97": 18, "133": 127, "103": 18, "73": 21, "43": 1, "109": 12, "63": 37, "79": 21, "48": 10, "115": 12, "53": 16, "127": 39, "121": 39, "58": 19, "91": 3, "28": 0, "85": 3}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
