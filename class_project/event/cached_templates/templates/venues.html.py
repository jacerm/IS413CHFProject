# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456156944.0031753
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/event/templates/venues.html'
_template_uri = 'venues.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['left_aside', 'main', 'content_head', 'right_aside']


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
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        venues = context.get('venues', UNDEFINED)
        def main():
            return render_main(context._locals(__M_locals))
        def content_head():
            return render_content_head(context._locals(__M_locals))
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
        venues = context.get('venues', UNDEFINED)
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n<a href="/event/venues.create/" class="btn btn-primary" style="margin-bottom: 15px;">Create New Venue</a>\r\n   <table class="table table-striped">\r\n       <tr>\r\n           <th>Name</th>\r\n           <th>Address</th>\r\n           <th>City</th>\r\n           <th>State</th>\r\n           <th>Zip</th>\r\n           <th>Actions</th>\r\n       </tr>\r\n')
        for venue in venues:
            __M_writer('       <tr>\r\n           <td>')
            __M_writer(str(venue.name))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(venue.address))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(venue.city))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(venue.state))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(venue.zip))
            __M_writer('</td>\r\n           <td><a href="/event/venues.edit/')
            __M_writer(str(venue.id))
            __M_writer('/">Edit</a> | <a class="venues_delete_link" href="/event/venues.delete/')
            __M_writer(str(venue.id))
            __M_writer('/">Delete</a></td>\r\n       </tr>\r\n')
        __M_writer('   </table>\r\n   \r\n<div class="modal fade" id="venues_delete_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n  <div class="modal-dialog" role="document">\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        Delete This Venue?\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="venues_confirm_delete_modal" href="" class="btn btn-danger">Delete</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Venues</h3>\r\n    </div>\r\n')
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
{"line_map": {"67": 9, "133": 127, "73": 9, "79": 12, "86": 12, "87": 23, "88": 24, "89": 25, "90": 25, "91": 26, "92": 26, "93": 27, "94": 27, "95": 28, "96": 28, "97": 29, "98": 29, "99": 30, "100": 30, "101": 30, "102": 30, "103": 33, "28": 0, "42": 1, "109": 3, "47": 7, "115": 3, "52": 10, "121": 54, "57": 52, "127": 54}, "filename": "C:/source/class/IS413/class_project/class_project/event/templates/venues.html", "source_encoding": "utf-8", "uri": "venues.html"}
__M_END_METADATA
"""
