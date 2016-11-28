#!/usr/bin/env python3

#!/usr/bin/env python3


# Charles Robison
# Session 07
# HTML Render Lab
class TextWrapper:
    """
    Added from solutions but not clear on what this is...

    A simple wrapper that creates a class with a render method
    for just text

    This allows the Element classes to render either Element objects or
    plain text

    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind = ""):
        file_out.write(current_ind + self.text)

class Element:
    tag = "html"
    indent = "    "
    def __init__(self, content = None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def make_tags(self):
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)
        return open_tag, close_tag

    def render(self, out_file, current_ind=""):
        print("in render, type of self", type(self))
        open_tag, close_tag = self.make_tags()
        out_file.write(current_ind + open_tag + "\n")
        for stuff in self.content:
            stuff.render(out_file, current_ind + self.indent)
            out_file.write("\n")
        out_file.write(current_ind + close_tag)


class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def render(self, out_file, ind=""):
        open_tag, close_tag = self.make_tags()
        out_file.write(ind + open_tag)
        for stuff in self.content:
            stuff.render(out_file)
        out_file.write(close_tag)

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, out_file, ind=""):
        open_tag, _ = self.make_tags()
        out_file.write(ind + open_tag.replace(">", " />"))

class Br(SelfClosingTag):
    tag = "br"

