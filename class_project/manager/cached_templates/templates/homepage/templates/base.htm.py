# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456020646.4563372
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['main', 'nav', 'right_aside', 'title', 'left_aside', 'content_head']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        def content_head():
            return render_content_head(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        def nav():
            return render_nav(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/loadmodal.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/ajaxform.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/moment.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/datetimepicker.js"></script>\r\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/datetimepicker.css" rel="stylesheet">\r\n    <link rel="icon" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/gengar.jpg" type="image/x-icon">\r\n  \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n  <body>\r\n    <header>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\r\n        <div id="maintenance" class="text-center">\r\n        </div>\r\n    </header>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_head'):
            context['self'].content_head(**pageargs)
        

        __M_writer('\r\n\r\n    <div class="container">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_aside'):
            context['self'].left_aside(**pageargs)
        

        __M_writer('\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'main'):
            context['self'].main(**pageargs)
        

        __M_writer('\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_aside'):
            context['self'].right_aside(**pageargs)
        

        __M_writer('\r\n    </div>\r\n\r\n    <footer class="container" style="margin-top: 15px;">\r\n        ')
 
        import datetime
        current_year =  datetime.date.today().year 
                
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime','current_year'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n        <hr/>\r\n        Copyright &copy; ')
        __M_writer(str(current_year))
        __M_writer(' - Colonial Heritage Foundation\r\n    </footer>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n            Main content goes here\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\r\n            Nav info goes here\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_aside(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_aside():
            return render_right_aside(context)
        __M_writer = context.writer()
        __M_writer('\r\n            Right aside content goes here\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_aside(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_aside():
            return render_left_aside(context)
        __M_writer = context.writer()
        __M_writer('\r\n            Left aside content goes here\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "line_map": {"128": 32, "134": 50, "140": 50, "17": 4, "146": 11, "19": 0, "152": 11, "158": 44, "164": 44, "39": 2, "40": 4, "41": 5, "170": 39, "45": 5, "176": 39, "50": 13, "51": 16, "52": 18, "53": 18, "54": 19, "55": 19, "56": 20, "57": 20, "58": 21, "59": 21, "60": 23, "61": 23, "62": 24, "63": 24, "64": 27, "65": 27, "66": 27, "182": 176, "71": 34, "76": 41, "81": 46, "86": 49, "91": 52, "92": 56, "99": 59, "100": 61, "101": 61, "102": 64, "103": 64, "104": 64, "110": 47, "116": 47, "122": 32}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
