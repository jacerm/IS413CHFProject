# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1454636012.7321901
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/base.htm'
_template_uri = 'homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['title', 'content_head', 'left_aside', 'main', 'right_aside', 'nav']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content_head():
            return render_content_head(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        def nav():
            return render_nav(context._locals(__M_locals))
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
        __M_writer('homepage/media/ajaxform.js"></script>\r\n    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">\r\n    <link rel="icon" href="')
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
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['current_year','datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n        <hr/>\r\n        Copyright &copy; ')
        __M_writer(str(current_year))
        __M_writer(' - Colonial Heritage Foundation\r\n    </footer>\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  </body>\r\n</html>')
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


"""
__M_BEGIN_METADATA
{"filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/base.htm", "line_map": {"128": 41, "65": 31, "70": 38, "75": 43, "140": 44, "158": 47, "80": 46, "17": 4, "146": 44, "19": 0, "85": 49, "86": 53, "152": 47, "93": 56, "94": 58, "95": 58, "96": 61, "97": 61, "98": 61, "164": 29, "134": 41, "116": 36, "39": 2, "40": 4, "41": 5, "122": 36, "45": 5, "110": 11, "176": 170, "104": 11, "50": 13, "51": 16, "52": 18, "53": 18, "54": 19, "55": 19, "56": 21, "57": 21, "58": 24, "59": 24, "60": 24, "170": 29}, "uri": "homepage/templates/base.htm", "source_encoding": "utf-8"}
__M_END_METADATA
"""
