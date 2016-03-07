# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456293840.3150916
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/event/templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content_head', 'main', 'left_aside', 'right_aside']


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
        areas = context.get('areas', UNDEFINED)
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Edit Event Page</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        areas = context.get('areas', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="POST" style="margin-left: 150px;">\r\n        <table>\r\n            ')
        __M_writer(str(form))
        __M_writer('\r\n        </table>\r\n        <input class="btn btn-primary" type="submit" value="Update" style="margin-top: 20px;">\r\n    </form>\r\n    \r\n    <div class="container text-center" style="margin-top: 15px;">\r\n      <h3>Areas</h3>\r\n    </div>\r\n    <a href="/event/events.createarea/" class="btn btn-primary" style="margin-bottom: 15px;">Create New Area</a>\r\n    <table class="table table-striped">\r\n       <tr>\r\n           <th>Name</th>\r\n           <th>Description</th>\r\n           <th>Place Number</th>\r\n           <th>Actions</th>\r\n       </tr>\r\n')
        for area in areas:
            __M_writer('       <tr>\r\n           <td>')
            __M_writer(str(area.name))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(area.description))
            __M_writer('</ts>\r\n           <td>')
            __M_writer(str(area.place_number))
            __M_writer('</td>\r\n           <td><a href="/event/events.editarea/')
            __M_writer(str(area.id))
            __M_writer('/">Edit</a> | <a class="areas_delete_link" href="/event/events.areadelete/')
            __M_writer(str(area.id))
            __M_writer('/">Delete</a></td>\r\n       </tr>\r\n')
        __M_writer('   </table>\r\n   \r\n<div class="modal fade" id="areas_delete_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n  <div class="modal-dialog" role="document">\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        Delete This Area?\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="areas_confirm_delete_modal" href="" class="btn btn-danger">Delete</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n    <script type="text/javascript">\r\n        $(function () {\r\n            $(\'#datetimepicker5\').datetimepicker({\r\n                format: "MM/DD/YYYY"\r\n            });\r\n            $(\'#datetimepicker6\').datetimepicker({\r\n                format: "MM/DD/YYYY"\r\n            });\r\n        });\r\n    </script>\r\n')
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
{"uri": "events.edit.html", "filename": "C:/source/class/IS413/class_project/class_project/event/templates/events.edit.html", "line_map": {"68": 3, "133": 127, "74": 3, "80": 12, "88": 12, "89": 15, "90": 15, "91": 31, "92": 32, "93": 33, "94": 33, "95": 34, "96": 34, "97": 35, "98": 35, "99": 36, "100": 36, "101": 36, "102": 36, "103": 39, "28": 0, "43": 1, "109": 9, "48": 7, "115": 9, "53": 10, "121": 70, "58": 68, "127": 70}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
