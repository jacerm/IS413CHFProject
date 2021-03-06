# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1456759561.2030787
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/catalog/templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['left_aside', 'right_aside', 'main', 'content_head']


from catalog import models as cmod 

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
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def main():
            return render_main(context._locals(__M_locals))
        isinstance = context.get('isinstance', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content_head():
            return render_content_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
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
        products = context.get('products', UNDEFINED)
        def main():
            return render_main(context)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<a href="/catalog/products.create/" class="btn btn-primary" style="margin-bottom: 15px;">Create New Product</a>\r\n   <table class="table table-striped">\r\n       <tr>\r\n           <th>Name</th>\r\n           <th>Type</th>\r\n           <th>Image</th>\r\n           <th>Quantity</th>\r\n           <th>Actions</th>\r\n       </tr>\r\n')
        for product in products:
            __M_writer('       <tr>\r\n           <td>')
            __M_writer(str(product.name))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(product.__class__.__name__))
            __M_writer('</td>\r\n           <td>')
            __M_writer(str(product.image))
            __M_writer('</td>\r\n           <td>\r\n')
            if isinstance(product, cmod.BulkProduct):
                __M_writer('                <span id="quantity_val">14</span> <span data-id=')
                __M_writer(str(product.id))
                __M_writer(' href="/catalog/products.getQuantity/')
                __M_writer(str(product.id))
                __M_writer('" class="glyphicon glyphicon-refresh quantity_btn"></span>\r\n')
            __M_writer('           </td>\r\n           <td><a href="/catalog/products.edit/')
            __M_writer(str(product.id))
            __M_writer('/">Edit</a> | <a class="products_delete_link" href="/catalog/products.delete/')
            __M_writer(str(product.id))
            __M_writer('/">Delete</a></td>\r\n       </tr>\r\n')
        __M_writer('   </table>\r\n   \r\n<div class="modal fade" id="products_delete_modal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\r\n  <div class="modal-dialog" role="document">\r\n    <div class="modal-content">\r\n      <div class="modal-header">\r\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\r\n      </div>\r\n      <div class="modal-body">\r\n        Delete This Product?\r\n      </div>\r\n      <div class="modal-footer">\r\n        <a id="products_confirm_delete_modal" href="" class="btn btn-danger">Delete</a>\r\n        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n      </div>\r\n    </div>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_head():
            return render_content_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Products</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/source/class/IS413/class_project/class_project/catalog/templates/products.html", "line_map": {"129": 4, "115": 30, "71": 10, "77": 10, "109": 26, "141": 135, "17": 1, "83": 57, "110": 27, "89": 57, "135": 4, "30": 0, "95": 13, "103": 13, "104": 23, "105": 24, "106": 25, "107": 25, "108": 26, "45": 1, "46": 2, "111": 27, "112": 29, "113": 30, "114": 30, "51": 8, "116": 30, "117": 30, "118": 32, "119": 33, "56": 11, "121": 33, "122": 33, "123": 36, "61": 55, "120": 33}, "uri": "products.html", "source_encoding": "utf-8"}
__M_END_METADATA
"""
