#!/usr/bin/env python3

'''
Given formatted input, will write out a properly formatted html file

Unit tests using PyTest:
    py.test test_html_render.py

Running tests using ipython:
    run run_html_render.py
    Creates -> test_html_output<step #>.html
'''

# AFAICT this does NOT include code review

class Element:
    # Class names should normally use the CapWords convention
    # Class attributes are shared by all instances
    tag = 'html'            # Element doesn't really have a tag
    indent_amount = '    '  # Indent increment
    current_indent = ''     # Indent accumulates as passed through

    # The __init__ method gets called when memory for the object is allocated

    def __init__(self, content=None, **kwargs):
        # Instance attributes are unique to each instance
        self.content = []
        if content:
            self.content.append(content)
        # Build single string for html attributes
        l = []  # Local, won't exist outside this method
        for entry, val in kwargs.items():
            l.append(' ' + entry + '="' + val + '"')
        self.html_attr = ' '.join(l)
        # build tags
        self.tag_open = '<{}{}>\n'.format(self.tag, self.html_attr)
        self.tag_open_single_line = '<{}{}>'.format(self.tag, self.html_attr)
        self.tag_close = '</{}>\n'.format(self.tag)
        self.tag_self_close = '<{}{} />\n'.format(self.tag, self.html_attr)
                        
    # Other Methods

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(str(content)) # Textwrapper, for render method
  
    # pass through current level of indentation
    def render(self, out_file, current_indent = ''):
        out_file.write(current_indent + self.tag_open)
        for content in self.content:
            if hasattr(content, 'render'):
                content.render(out_file, current_indent + self.indent_amount)
            else:
                out_file.write(current_indent + '    ' + content + '\n')
        out_file.write(current_indent + self.tag_close)

# === Sub Classes ===

class OneLineTag(Element):

    def render(self, out_file, current_indent = ''):
        out_file.write(current_indent + self.tag_open_single_line)
        for content in self.content:
            if hasattr(content, 'render'):
                content.render(out_file, '')
            else:
                out_file.write(' ' + content + ' ')
        out_file.write(self.tag_close)
        
class SelfClosingTag(Element):

    def render(self, out_file, current_indent = ''):
        out_file.write(current_indent + self.tag_self_close)
        for content in self.content:
            if hasattr(content, 'render'):
                content.render(out_file, '')
            else:
                out_file.write(' ' + content + ' ')
        # out_file.write('\n')

class Meta(SelfClosingTag):
    # Meta(charset="UTF-8")
    # <meta charset="UTF-8" />
    tag = 'meta'
    
    def render(self, out_file, current_indent = ''):
        content = ' charset="UTF-8'
        super(Meta, self).render(out_file, current_indent)

class Head(Element):
    tag = 'head'

class Html(Element):
    tag = 'html'
    
    def render(self, out_file, current_indent = ''):
        out_file.write('<!DOCTYPE html>\n')
        # LOL - using 'copy, paste & cross fingers':
        super(Html, self).render(out_file, current_indent)

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Title(OneLineTag):
    tag = 'title'

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    # A("http://google.com", "link")
    # <a href="http://google.com">link</a>
    tag = 'a'
    
    def __init__(self, html_attr, content):
        self.content = []
        if content:
            self.content.append(content)
        self.html_attr = ' href="' + html_attr + '"'
        self.tag_open_single_line = '<{}{}>'.format(self.tag, self.html_attr)
        self.tag_close = '</{}>\n'.format(self.tag)

class Ul(Element):
    # Ul(id="TheList", style="line-height:200%")
    # <ul style="line-height:200%" id="TheList">
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    # H(2, "PythonClass - Class 6 example")
    # <h2> PythonClass - Class 6 example </h2>

    def __init__(self, level, content):
        self.content = []
        if content:
            self.content.append(content)
        self.tag = 'h' + str(level)
        self.tag_open_single_line = '<{}>'.format(self.tag)
        # self.tag_open_single_line = '<{}{}>'.format(self.tag, self.html_attr)
        self.tag_close = '</{}>\n'.format(self.tag)
