"""Dec 2, 2016 HTML renderer lab exercise."""

# class TextWrapper:
#     """
#     A simple wrapper that creates a class with a render method
#     for just text

#     This allows the Element classes to render either Element objects or
#     plain text

#     """
#     def __init__(self, text):
#         self.text = text

#     def render(self, file_out, current_ind=""):
#         file_out.write(current_ind + self.text)


class Element:
    tag = "html"
    ind = "    "

    def __init__(self, content="", **kwargs):
        self.content = []
        # print(kwargs)
        if content.strip():
            self.content.append(content)
        self.kwargs = kwargs


    def append(self, content=""):
        self.content.append(content)
        # if hasattr(content, 'render'):
        #     self.content.append(content)
        # else:
        #     print("hello")


    def render(self, html_out, ind=""):
        # print("Rendering ind, self:", len(ind), self)
        # print("html_out.getvalue:", repr(html_out.getvalue()))
        html_out.write(ind)
        # print("After ind:", repr(html_out.getvalue()))
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.kwargs.items()])
        # print(self.kwargs)
        html_out.write("<" + self.tag + attrs + ">""\n")
        # print("before try:", self.content)
        for content in self.content:
            try:
                # print("inside try:", repr(html_out.getvalue()))
                content.render(html_out, ind + self.ind)
            except AttributeError:
                html_out.write(ind + self.ind + content)
                html_out.write("\n")
        html_out.write(ind + "</" + self.tag + ">" + "\n")

class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"

class OneLineTag(Element):
    def __init__(self, content="", **kwargs):
        # self.intv = intv
        if content.strip():
            self.content = content
        self.kwargs = kwargs

    def render(self, html_out, ind=""):
        html_out.write(ind)
        html_out.write("<" + self.tag + ">")
        for content in self.content:
            html_out.write(content)
        html_out.write("</" + self.tag + ">" + "\n")

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):
    def render(self, html_out, ind=""):
        html_out.write(ind)
        attrs = "".join([' {}="{}"'.format(key, val) for key, val in self.kwargs.items()])
        html_out.write("<" + self.tag + attrs + "/>" + "\n")

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(Element):
    tag = 'a'
    def __init__(self, link, content):
        self.link = link
        self.content = content
        Element.__init__(self, content, href=self.link)

class Ul(Element):
    tag = 'Ul'

class Li(Element):
    tag = 'Li'

class Header(OneLineTag):
    tag = 'h'
    def __init__(self, intv, content):
        self.intv = intv
        if content.strip():
            self.content = content
        self.tag = 'h' + str(intv)
        OneLineTag.__init__(self, content)

class Doctype(Element):
    tag = 'DOCTYPE html'
    # def render(self, content):
    def render(self, html_out, ind=""):
        # self.content = content
        html_out.write("<" + "!" + self.tag)
        # html_out.write('html')
        html_out.write(">" + "\n")
        # Element.render(self, html_out)

class Encoding(SelfClosingTag):
    tag = 'meta'


def main():

    f = open('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session7/html_renderer_output.html', 'w')

    dt = Doctype()
    h = Html()
    hd = Head()
    encode_attributes = dict(charset="UTF-8")
    e = Encoding(**encode_attributes)
    t = Title("PythonClass - Session6")
    b = Body()
    header = Header(2, "Text for header")
    p_attributes = dict(style="text-align: center; font-style: oblique;", clas= 'intro')
    p = P("Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text",
          **p_attributes)
    hr = Hr()
    br = Br()
    ul_attributes = dict(style="line-height:200%", id="TheList")
    ul = Ul(**ul_attributes)
    li1 = Li("The first item in a list",)
    li2_attributes = dict(style="color: red")
    li2 = Li("This is the second item", **li2_attributes)
    li3 = Li("And this is a")
    a = A("http://google.com", "link to google")

    dt.render(f)
    h.append(hd)
    hd.append(e)
    hd.append(t)
    h.append(b)
    b.append(header)
    b.append(p)
    b.append(hr)
    b.append(br)
    b.append(ul)
    ul.append(li1)
    ul.append(li2)
    ul.append(li3)
    li3.append(a)
    h.render(f)
    f.close()
