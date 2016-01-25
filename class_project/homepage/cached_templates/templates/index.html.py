# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453388919.0847068
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['nav_links', 'left_aside', 'right_aside', 'main', 'content_head']


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
        def content_head():
            return render_content_head(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
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
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-sm-12 center_divider">\r\n        <h3>Colonial Heritage Foundation</h3>\r\n        <p>Colonial Heritage Foundation is a patriotic company that displays custom made colonial replicas and renactments</p>\r\n        \r\n        <p class="">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut egestas sem a vestibulum tempus. Curabitur tempor massa ut mauris hendrerit sodales. Aliquam non sapien eget nisi sollicitudin tempus. Nam a lorem id ex commodo tempus at id lorem. Nam a felis sed lectus molestie consequat sit amet id sem. Aenean lectus metus, congue eu ultrices nec, lacinia nec justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aenean in rutrum arcu. Sed at magna vitae neque venenatis fermentum. In efficitur sollicitudin vulputate. Pellentesque nisl quam, accumsan nec elit eu, rhoncus aliquam mauris. Proin a est imperdiet, ultrices nisi ut, consequat mauris. Praesent rhoncus sodales velit a mattis. Sed eget eros sit amet purus imperdiet lobortis dapibus imperdiet mi. Aenean varius luctus ante, sit amet pharetra magna fringilla sit amet. Nullam ut pharetra elit.Nunc vitae blandit lorem. Curabitur pharetra vulputate eleifend. Vivamus hendrerit neque eros, nec vestibulum ipsum euismod sit amet. Morbi et rutrum sapien, id semper dolor. Curabitur nec hendrerit est, at aliquet dui. Pellentesque dapibus efficitur tortor, sit amet aliquam est facilisis auctor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere eget dui non lacinia. Proin iaculis dui augue, et facilisis odio cursus sit amet. Sed ultricies ultricies aliquet. Donec imperdiet mauris id dui lobortis, ac dictum risus scelerisque. Sed convallis placerat ante quis dapibus.Etiam nec est feugiat, finibus velit at, dignissim magna. Sed tincidunt posuere tortor. Cras pharetra varius cursus. Proin tempor eleifend diam. Mauris sit amet scelerisque tellus, eget gravida libero. Vivamus congue gravida ultricies. Donec neque est, bibendum quis tincidunt non, malesuada vel tortor. Donec vel nisl urna. Maecenas convallis risus id nulla rutrum sodales. Sed id metus vulputate metus mattis porta sit amet a elit. Nullam nec convallis lorem, imperdiet laoreet metus.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed accumsan eleifend dui, nec auctor lacus semper eget. Proin convallis consectetur tortor, vitae ultrices nisi pharetra non. Mauris laoreet urna in nulla consectetur, sed maximus lectus consequat. Etiam gravida pharetra urna, et rhoncus ante tristique et. Nam sollicitudin porttitor varius. Quisque cursus libero vel ligula luctus, et congue velit iaculis. Quisque ut urna sit amet tortor aliquam lacinia. Vestibulum in nisl at dolor euismod luctus.</p>\r\n        \r\n        <p class="">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut egestas sem a vestibulum tempus. Curabitur tempor massa ut mauris hendrerit sodales. Aliquam non sapien eget nisi sollicitudin tempus. Nam a lorem id ex commodo tempus at id lorem. Nam a felis sed lectus molestie consequat sit amet id sem. Aenean lectus metus, congue eu ultrices nec, lacinia nec justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aenean in rutrum arcu. Sed at magna vitae neque venenatis fermentum. In efficitur sollicitudin vulputate. Pellentesque nisl quam, accumsan nec elit eu, rhoncus aliquam mauris. Proin a est imperdiet, ultrices nisi ut, consequat mauris. Praesent rhoncus sodales velit a mattis. Sed eget eros sit amet purus imperdiet lobortis dapibus imperdiet mi. Aenean varius luctus ante, sit amet pharetra magna fringilla sit amet. Nullam ut pharetra elit.Nunc vitae blandit lorem. Curabitur pharetra vulputate eleifend. Vivamus hendrerit neque eros, nec vestibulum ipsum euismod sit amet. Morbi et rutrum sapien, id semper dolor. Curabitur nec hendrerit est, at aliquet dui. Pellentesque dapibus efficitur tortor, sit amet aliquam est facilisis auctor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere eget dui non lacinia. Proin iaculis dui augue, et facilisis odio cursus sit amet. Sed ultricies ultricies aliquet. Donec imperdiet mauris id dui lobortis, ac dictum risus scelerisque. Sed convallis placerat ante quis dapibus.Etiam nec est feugiat, finibus velit at, dignissim magna. Sed tincidunt posuere tortor. Cras pharetra varius cursus. Proin tempor eleifend diam. Mauris sit amet scelerisque tellus, eget gravida libero. Vivamus congue gravida ultricies. Donec neque est, bibendum quis tincidunt non, malesuada vel tortor. Donec vel nisl urna. Maecenas convallis risus id nulla rutrum sodales. Sed id metus vulputate metus mattis porta sit amet a elit. Nullam nec convallis lorem, imperdiet laoreet metus.Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed accumsan eleifend dui, nec auctor lacus semper eget. Proin convallis consectetur tortor, vitae ultrices nisi pharetra non. Mauris laoreet urna in nulla consectetur, sed maximus lectus consequat. Etiam gravida pharetra urna, et rhoncus ante tristique et. Nam sollicitudin porttitor varius. Quisque cursus libero vel ligula luctus, et congue velit iaculis. Quisque ut urna sit amet tortor aliquam lacinia. Vestibulum in nisl at dolor euismod luctus.</p>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Welcome</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 12, "80": 3, "98": 32, "68": 33, "134": 128, "104": 32, "28": 0, "74": 3, "43": 1, "110": 21, "48": 10, "116": 21, "53": 16, "86": 18, "58": 19, "92": 18, "122": 12, "63": 30}, "source_encoding": "utf-8", "filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/index.html", "uri": "index.html"}
__M_END_METADATA
"""
