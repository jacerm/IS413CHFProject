# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456252521.484208
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/event/templates/events.create.html'
_template_uri = 'events.create.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['left_aside', 'main', 'right_aside', 'content_head']


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
    return runtime._inherit_from(context, 'homepage/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def content_head():
            return render_content_head(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
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


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="POST" style="margin-left: 150px;">\r\n        <table>\r\n            ')
        __M_writer(str(form))
        __M_writer('\r\n        </table>\r\n        <input class="btn btn-primary" type="submit" value="Create" style="margin-top: 20px;">\r\n    </form>\r\n    <script type="text/javascript">\r\n        $(function () {\r\n            $(\'#datetimepicker3\').datetimepicker({\r\n                format: "MM/DD/YYYY"\r\n            });\r\n            $(\'#datetimepicker4\').datetimepicker({\r\n                format: "MM/DD/YYYY"\r\n            });\r\n        });\r\n    </script>\r\n')
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


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Create New Event Page</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.create.html", "line_map": {"67": 9, "100": 31, "118": 112, "73": 9, "42": 1, "79": 12, "112": 3, "52": 10, "86": 12, "87": 15, "88": 15, "57": 29, "47": 7, "28": 0, "106": 3, "94": 31}, "source_encoding": "utf-8", "filename": "C:/source/class/IS413/class_project/class_project/event/templates/events.create.html"}
__M_END_METADATA
"""
