# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454635447.6752553
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main', 'right_aside', 'content_head', 'left_aside']


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
        def content_head():
            return render_content_head(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        __M_writer = context.writer()
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
        __M_writer('\r\n    <div class="col-sm-8 center_divider">\r\n        <h3 class="text-center">Center</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_aside(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_aside():
            return render_right_aside(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-sm-2 right_divider">\r\n        <h3 class="text-center">Right</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Sections Page</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_aside(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_aside():
            return render_left_aside(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-sm-2 left_divider">\r\n        <h3 class="text-center">Left</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/sections.html", "line_map": {"96": 3, "66": 15, "102": 9, "72": 15, "41": 1, "108": 9, "78": 21, "114": 108, "51": 13, "84": 21, "46": 7, "56": 19, "90": 3, "28": 0}, "uri": "sections.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
