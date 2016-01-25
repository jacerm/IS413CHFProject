# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1453389704.3257875
_enable_loop = True
_template_filename = 'C:/source/class/IS413/class_project/class_project/homepage/templates/terms.html'
_template_uri = 'terms.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['nav_links', 'main', 'left_aside', 'right_aside', 'content_head']


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
        def main():
            return render_main(context._locals(__M_locals))
        def left_aside():
            return render_left_aside(context._locals(__M_locals))
        def right_aside():
            return render_right_aside(context._locals(__M_locals))
        def content_head():
            return render_content_head(context._locals(__M_locals))
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


def render_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def main():
            return render_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="col-sm-12 center_divider">\r\n        <h3>Web Site Terms and Conditions of Use</h3>\r\n        <p>The following terms and conditions (the "Terms and Conditions") govern your use of this web site, and any content made available from or through this web site, including any subdomains thereof (the "Web Site"). The Web Site is made available by Time Inc. ("Time Inc." or "we" or "us"). We may change the Terms and Conditions from time to time, at any time without notice to you, by posting such changes on the Web Site. BY USING THE WEB SITE, YOU ACCEPT AND AGREE TO THESE TERMS AND CONDITIONS AS APPLIED TO YOUR USE OF THE WEB SITE. If you do not agree to these Terms and Conditions, you may not access or otherwise use the Web Site.</p>\r\n        <ol>\r\n            <li class="list_item first_list_item"><u><b>Proprietary Rights.</b></u> As between you and Time Inc., Time Inc. owns, solely and exclusively, all rights, title and interest in and to the Web Site, all the content (including, for example, audio, photographs, illustrations, graphics, other visuals, video, copy, text, software, titles, Shockwave files, etc.), code, data and materials thereon, the look and feel, design and organization of the Web Site, and the compilation of the content, code, data and materials on the Web Site, including but not limited to any copyrights, trademark rights, patent rights, database rights, moral rights, sui generis rights and other intellectual property and proprietary rights therein. Your use of the Web Site does not grant to you ownership of any content, code, data or materials you may access on or through the Web Site.</li>\r\n            \r\n            <li class="list_item"><u><b>Limited License.</b></u> You may access and view the content on the Web Site on your computer or other device and, unless otherwise indicated in these Terms and Conditions or on the Web Site, make single copies or prints of the content on the Web Site for your personal, internal use only. Use of the Web Site and the services offered on or through the Web Site, are only for your personal, non-commercial use.</li>\r\n        \r\n            <li class="list_item"><u><b>Prohibited Use.</b></u> Any commercial or promotional distribution, publishing or exploitation of the Web Site, or any content, code, data or materials on the Web Site, is strictly prohibited unless you have received the express prior written permission from authorized personnel of Time Inc. or the otherwise applicable rights holder. Other than as expressly allowed herein, you may not download, post, display, publish, copy, reproduce, distribute, transmit, modify, perform, broadcast, transfer, create derivative works from, sell or otherwise exploit any content, code, data or materials on or available through the Web Site. You further agree that you may not alter, edit, delete, remove, otherwise change the meaning or appearance of, or repurpose, any of the content, code, data, or other materials on or available through the Web Site, including, without limitation, the alteration or removal of any trademarks, trade names, logos, service marks, or any other proprietary content or proprietary rights notices. You acknowledge that you do not acquire any ownership rights by downloading any copyrighted material from or through the Web Site. If you make other use of the Web Site, or the content, code, data or materials thereon or available through the Web Site, except as otherwise provided above, you may violate copyright and other laws of the United States, other countries, as well as applicable state laws and may be subject to liability for such unauthorized use.</li>\r\n            \r\n            <li class="list_item"><u><b>Trademarks.</b></u> The trademarks, logos, service marks and trade names (collectively the "Trademarks") displayed on the Web Site or on content available through the Web Site are registered and unregistered Trademarks of Time Inc. and others and may not be used in connection with products and/or services that are not related to, associated with, or sponsored by their rights holders that are likely to cause customer confusion, or in any manner that disparages or discredits their rights holders. All Trademarks not owned by Time Inc. that appear on the Web Site or on or through the Web Site\'s services, if any, are the property of their respective owners. Nothing contained on the Web Site should be construed as granting, by implication, estoppel, or otherwise, any license or right to use any Trademark displayed on the Web Site without the written permission of Time Inc. or the third party that may own the applicable Trademark. Your misuse of the Trademarks displayed on the Web Site or on or through any of the Web Site\'s services is strictly prohibited.</li>\r\n        </ol>\r\n    </div>\r\n')
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
        __M_writer('\r\n    <div class="container text-center">\r\n      <h3>Terms</h3>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"97": 18, "133": 127, "103": 18, "73": 3, "43": 1, "109": 37, "63": 35, "79": 3, "48": 10, "115": 37, "53": 16, "127": 12, "121": 12, "58": 19, "91": 21, "28": 0, "85": 21}, "source_encoding": "utf-8", "filename": "C:/source/class/IS413/class_project/class_project/homepage/templates/terms.html", "uri": "terms.html"}
__M_END_METADATA
"""
