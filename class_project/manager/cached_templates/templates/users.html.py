# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456255023.6241012
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/manager/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main', 'left_aside', 'right_aside', 'content_head']


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
        def main():
            return render_main(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def content_head():
            return render_content_head(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n   <a href="/manager/users.create/" class="btn btn-primary" style="margin-bottom: 15px;">Create New User</a>\r\n   <table class="table table-striped">\r\n       <tr>\r\n           <th>Username</th>\r\n           <th>First Name</th>\r\n           <th>Last Name</th>\r\n           <th>Email</th>\r\n           <th>Groups</th>\r\n           <th>Actions</th>\r\n       </tr>\r\n')
        for user in users:
            __M_writer('       <tr>\r\n           <td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n           <td>\r\n')
            for group in user.groups.all():
                __M_writer('                ')
                __M_writer(str(group.name))
                __M_writer('\r\n')
            __M_writer('           </td>\r\n           <td><a href="/manager/users.edit/')
            __M_writer(str(user.id))
            __M_writer('/">Edit</a> | <a class="users_delete_link" href="/manager/users.delete/')
            __M_writer(str(user.id))
            __M_writer('/">Delete</a></td>\r\n       </tr>\r\n')
        __M_writer('   </table>\r\n   \r\n<div class="modal fade" id="users_delete_Modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n  <div class="modal-dialog" role="document">\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        Delete This User?\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="users_confirm_delete_modal" href="" class="btn btn-danger">Delete</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n')
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


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Users</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "users.html", "source_encoding": "utf-8", "filename": "C:/source/class/IS413/class_project/class_project/manager/templates/users.html", "line_map": {"130": 3, "67": 12, "136": 130, "74": 12, "75": 23, "76": 24, "77": 25, "78": 25, "79": 26, "80": 26, "81": 27, "82": 27, "83": 28, "84": 28, "85": 30, "86": 31, "87": 31, "88": 31, "89": 33, "90": 34, "91": 34, "28": 0, "93": 34, "94": 37, "100": 9, "92": 34, "42": 1, "47": 7, "112": 58, "52": 10, "118": 58, "57": 56, "124": 3, "106": 9}}
__M_END_METADATA
"""
