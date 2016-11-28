"""
test code for html_render.py
"""

# Charles Robison
# Session 07
# HTML Render Lab

from html_render import Element, Html, Body, P, Head
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

def test_head():
    outfile = io.StringIO()

    e = Head("this is some text")
    e.append("and this is some more text")
    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents












