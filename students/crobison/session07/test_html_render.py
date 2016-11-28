"""
test code for html_render.py
"""

# Charles Robison
# Session 07
# HTML Render Lab

from html_render import Element, Html, Body, P, TextWrapper, Head, Title
import io

def render_result(element, ind=""):
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()

def test_init():
    e = Element()

    e = Element("this is some text")

# def test_content():
#     # fixme: this tests internals!!!
#     e = Element("this is some text")

#     assert "this is some text" in e.content

# def test_append():
#     e = Element("this is some text")
#     e.append("some more text")

#     assert "some more text" in e.content

def test_two_instances():
    e = Element("this is some text")
    e2 = Element("this is some text")

    e.append("some more text")

    assert "some more text" not in e2.content

def test_render():
    outfile = io.StringIO()

    e = Element("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")

# def test_html():
#     outfile = io.StringIO()

#     e = Html("this is some text")
#     e.append("and this is some more text")
#     e.render(outfile)

#     outfile.seek(0)
#     file_contents = outfile.read()

#     assert("this is some text") in file_contents
#     assert("and this is some more text") in file_contents

    # print(file_contents)
    # assert False
    #assert file_contents.startswith("<html>")
    #assert file_contents.strip().endswith("</html>")

def test_body():
    outfile = io.StringIO()
    
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.strip().endswith("</body>")

    # print(file_contents)
    # assert False
    #assert file_contents.startswith("<body>")
    #assert file_contents.strip().endswith("</body>")

def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e)

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # print(file_contents)
    # assert False
    #assert file_contents.startswith("<p>")
    #assert file_contents.strip().endswith("</p>")

def test_text_wrapper():
    tw = TextWrapper("A basic piece of text")

    file_contents = render_result(tw)
    assert file_contents == "A basic piece of text"

def text_sub_element():
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")

    file_contents = render_result(page)

    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents

def test_step_2_noindent():
    page = Html()
    body = Body()
    page.append(body)
    body.append(P("a small paragraph of text"))
    body.append(P("another small paragraph of text"))
    body.append(P("and here is a bit more"))

    file_contents = render_result(page).strip()

def test_indent():
    html = Html("some content")
    file_contents = render_result(html, ind="   ")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[0].startswith("   <")
    assert lines[-1].startswith("   <")

def test_indent_contents():
    html = Html("some content")
    file_contents = render_result(html, ind="")

    print(file_contents)
    lines = file_contents.split("\n")
    assert lines[1].startswith(Element.indent)

def test_mulitiple_indent():
    body = Body()
    body.append(P("some text"))
    html = Html(body)

    file_contents = render_result(html)

    print(file_contents)
    lines = file_contents.split("\n")
    for i in range(3):
        assert lines[i].startswith(i * Element.indent + "<")

    assert lines[3].startswith(3 * Element.indent + "some")

def test_title():
    t = Title("Some title text")
    file_contents = render_result(t, ind="   ")

    print(file_contents)

    assert "\n" not in  file_contents
    assert file_contents.startswith("   <title>")
    assert file_contents.endswith("</title>")
    assert "\n" not in file_contents


def test_head():
    outfile = io.StringIO()

    e = Head("this is some text")
    e.append("and this is some more text")
    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents












