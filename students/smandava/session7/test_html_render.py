"""
Dec 2, 2016 test code for html_render_new.py.
"""
import io

from html_render_new import Element, Html, Body, P, Head, Encoding, Title, Header, Hr, Br, Ul, Li, A, Doctype

def test_init():
    e = Element()
    e = Element("this is some text")

def test_content():
    # fixme: this tests internals!!!
    e = Element("this is some text")
    assert "this is some text" in e.content

def test_append():
    e = Element("this is some text")
    e.append("some more text")
    assert "some more text" in e.content

def test_two_instances():
        e = Element("this is some text")
        e2 = Element("this is some text")
        e.append("some more text")

        assert "some more text" not in e2.content

def test_render():
    outfile = io.StringIO()

    e = Element("this is some text")
    e.append("and this is some more text")
    # with open("test1.html", 'w') as outfile:
    e.render(outfile, "")

    (outfile.seek(0))
    file_contents = outfile.read()
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)

    assert file_contents.strip().startswith("<html>")
    assert file_contents.strip().endswith("</html>")

def test_html_body():
    outfile = io.StringIO()
    h = Html()
    b = Body("PythonClass - Session 6")
    h.append(b)
    h.render(outfile)
    file_output = outfile.getvalue()
    print(file_output)

    assert file_output.strip().startswith("<html>")
    assert file_output.strip().endswith("</html>")

def test_html_body_p():
    outfile = io.StringIO()
    h = Html()
    b = Body("PythonClass - Session 6")
    p = P("Here is a paragraph of text -- there could be more of them, but this is enough to show that we can do some text")
    h.append(b)
    b.append(p)
    b.append("Adding plain text for verification.")
    h.render(outfile)
    file_output = outfile.getvalue()
    print(file_output)

    assert file_output.strip().startswith("<html>")
    assert file_output.strip().endswith("</html>")
    assert "Adding plain text for verification" in file_output
    assert "<body>" in file_output

def test_indent():
    outfile = io.StringIO()
    p = P("Test contents")
    p.render(outfile, "  ")
    file_output = outfile.getvalue()
    lines = file_output.split("\n")
    print(file_output)
    assert file_output.startswith("  ")
    assert lines[1].startswith("      T")
    assert lines[2].startswith("  <")


def test_indent_subtag():
    outfile = io.StringIO()
    b = Body()
    b.append(P("Test contents."))
    b.render(outfile)
    file_output = outfile.getvalue()
    lines = file_output.split("\n")
    print(file_output)
    assert file_output.startswith("<body>")
    assert lines[1].startswith(Element.ind + "<p>")
    assert lines[2].startswith(Element.ind + b.ind + "T")
    assert lines[3].startswith(Element.ind + "</p>")
    assert lines[4].startswith("</body>")
    # assert False

def test_meta():
    outfile = io.StringIO()
    encode_attributes = dict(charset="UTF-8")
    e = Encoding(**encode_attributes)
    e.render(outfile)
    file_output = outfile.getvalue()
    print(file_output)
    assert 'meta charset="UTF-8"/' in file_output

def test_header():
    outfile = io.StringIO()
    header = Header(3, "Text for header")
    header.render(outfile)
    file_output = outfile.getvalue()
    print(file_output)
    assert "<h3>Text for header</h3>" in file_output

def test_anchor():
    outfile = io.StringIO()
    a = A("http://google.com", "link to google")
    a.render(outfile)
    file_output = outfile.getvalue()
    print(file_output)
    assert "http://google.com" in file_output

def test_empty_content():
    e = Element()
    assert bool(e.content) is False

def test_full_rendering():
    outfile = io.StringIO()
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

    dt.render(outfile)
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
    h.render(outfile)
    file_output = outfile.getvalue()
    lines = file_output.split("\n")
    print(file_output)
    assert file_output.startswith("<!DOCTYPE html>")
    assert lines[1].startswith("<html>")
    assert lines[2].startswith(h.ind + "<head>")
    assert lines[3].startswith(h.ind + hd.ind + "<meta")
    assert lines[4].startswith(h.ind + hd.ind + "<title")
    # The order of attributes passed in a dict can change resulting in test failure.
    assert 'p style="text-align: center; font-style: oblique;" clas="intro"' in file_output
    assert "Here is a paragraph" in file_output
    # The order of attributes passed in a dict can change resulting in test failure.
    assert 'Ul style="line-height:200%" id="TheList"' in file_output
    assert "<Li>" in file_output
    assert 'href="http://google.com"' in file_output
    assert file_output.strip().endswith("</html>")
