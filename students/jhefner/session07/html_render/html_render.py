#!/Users/jhefner/python_dev/uw_python/bin/python

class TextWrapper:
    def __init__(self, text):
        self.text = text

    def render(self, file_out, current_ind=""):
        file_out.write(current_ind + self.text)

class Element():
    html_tag = 'html'
    indent = '    '

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.content = []
        if content:
            self.append(content)

    def append(self,content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))

    def make_tags(self):
        attrs = " ".join(['{}="{}"'.format(key, val) for key, val in self.attributes.items()])
        if attrs.strip():
            open_tag= "<"+self.html_tag+" "+attrs.strip()+">"
        else:
            open_tag = "<"+self.html_tag+">"
        close_tag = "</"+self.html_tag+">"
        return open_tag, close_tag

    def render(self, out_file, ind=""):
        open_tag, close_tag = self.make_tags()
        out_file.write(ind+open_tag+"\n")
        for i in self.content:
            i.render(out_file, ind+self.indent)
            out_file.write("\n")
        out_file.write(ind+close_tag)

class OneLineTag(Element):
    def render(self, out_file, ind=""):
        open_tag, close_tag = self.make_tags()
        out_file.write(ind+open_tag)
        for i in self.content:
            i.render(out_file)
        out_file.write(close_tag)


class Title(OneLineTag):
    html_tag = 'title'

class Html(Element):
    html_tag = 'html'
    def render(self, file_out, ind=""):
        file_out.write(ind+"<!DOCTYPE html>\n")
        super().render(file_out, ind=ind)

class Body(Element):
    html_tag = 'body'

class P(Element):
    html_tag = 'p'

class Head(Element):
    html_tag = 'head'

class SelfClosingTag(Element):
    def render(self, out_file, ind=""):
        open_tag, _ = self.make_tags()
        out_file.write(ind+open_tag.replace(">"," />"))

class Hr(SelfClosingTag):
    html_tag = 'hr'

class Br(SelfClosingTag):
    html_tag = 'br'

class A(OneLineTag):
    html_tag = 'a'
    def __init__(self, link, content, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)

class Ul(Element):
    html_tag = 'ul'

class Li(Element):
    html_tag = 'li'

class H(OneLineTag):
    html_tag = 'H'
    def __init__(self, level, content=None, **kwargs):
        self.tag = 'h'+str(int(level))
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    html_tag = 'meta'
