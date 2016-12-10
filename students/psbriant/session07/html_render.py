"""
Name: Paul Briant
Date: 11/22/16
Class: Introduction to Python
Session07
LAB: HTML Renderer

Description:

"""
# -------------------------------Imports----------------------------------------


# -------------------------------Classes--------------------------------------
class TextWrapper:
    """
    Render either Element objects or plain text
    """
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)


class Element:

    tag = 'html'
    indent = "    "

    def __init__(self, content=None, **kwargs):
        """
        Initializes class attribute content and appends any value not equal to
        none into and empty list.
        """
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self, content):
        """
        Takes in new content in the form of a string and adds it to list of
        existing content.
        """
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def make_tags(self):
        """
        Generalizes the creation of tags and allows for tags to be created with
        or without attributes.
        """
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag = "<{} {}>".format(self.tag, attrs.strip())
        else:
            open_tag = "<{}>".format(self.tag)
        close_tag = "</{}>".format(self.tag)

        return open_tag, close_tag

    def render(self, file_out, ind=""):
        """
        Takes in the output file, generates opening and closing tags and
        inserts each individual line of content in between it. All tags and
        content are written to output file.
        """
        open_tag, close_tag = self.make_tags()
        file_out.write(ind + open_tag + "\n")
        for stuff in self.content:
            stuff.render(file_out, (ind + self.indent))
            file_out.write("\n")
        file_out.write(ind + close_tag)


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    def render(self, file_out, ind=""):
        """
        Takes in the output file, generates opening and closing tags and
        inserts each individual line of content in between it. All tags and
        content are written to output file.
        """
        open_tag, close_tag = self.make_tags()
        file_out.write(ind + open_tag)
        for stuff in self.content:
            stuff.render(file_out)
        file_out.write(close_tag)


class Title(OneLineTag):
    tag = 'title'


class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        """
        Take in an output file and generate a self closing tag.
        """
        file_out.write("{}<{} />".format((ind + self.indent), self.tag))


class Hr(SelfClosingTag):
    tag = 'hr'
    indent = ""


class Br(SelfClosingTag):
    tag = 'br'
    indent = ''


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        Element.__init__(self, content, **kwargs)


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(OneLineTag):
    tag = "H"

    def __init__(self, size, content=None, **kwargs):
        self.tag = "h" + str(int(size))
        super().__init__(content, **kwargs)
