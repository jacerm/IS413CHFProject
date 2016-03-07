# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456253834.1773903
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/manager/templates/users.edit.html'
_template_uri = 'users.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['left_aside', 'content_head', 'right_aside', 'main']


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
    return runtime._inherit_from(context, '/homepage/templates/app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_head():
            return render_content_head(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
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


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Manager Edit Page</h3>\r\n    </div>\r\n')
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


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <a href="/manager/users.passchange/')
        __M_writer(str( user.id ))
        __M_writer('" class="btn btn-primary">Update Password</a>\r\n    <form method="POST" style="margin-left: 150px;">\r\n        <table>\r\n            ')
        __M_writer(str(form))
        __M_writer('\r\n        </table>\r\n        <input class="btn btn-primary" type="submit" value="Update" style="margin-top: 20px;">\r\n    </form>\r\n    <script type="text/javascript">\r\n        $(function () {\r\n            $(\'#datetimepicker2\').datetimepicker({\r\n                format: "MM/DD/YYYY"\r\n            });\r\n        });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"80": 3, "98": 29, "68": 9, "104": 12, "28": 0, "74": 9, "43": 1, "112": 12, "48": 7, "113": 13, "114": 13, "115": 16, "116": 16, "53": 10, "86": 3, "58": 27, "92": 29, "122": 116}, "source_encoding": "utf-8", "uri": "users.edit.html", "filename": "C:/source/class/IS413/class_project/class_project/manager/templates/users.edit.html"}
__M_END_METADATA
"""
