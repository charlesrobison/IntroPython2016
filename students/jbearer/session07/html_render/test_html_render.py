#!/usr/bin/env python
"""
test code for html_render.py
"""
import io

from html_render import Element, Html, Body, P, Head, Title

def test_init():
    e = Element()

    e = Element("this is some text")


def test_content():
    # fixme: this tests internals!!!!
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

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")

def test_Html():
    outfile = io.StringIO()

    e = Html('This is some text')
    e.append('This is some more text')

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is some text') in file_contents
    assert('This is some more text') in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")

def test_Body():
    outfile = io.StringIO()

    e = Body('This is some text')
    e.append('This is some more text')

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is some text') in file_contents
    assert('This is some more text') in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.strip().endswith("</body>")

def test_P():
    outfile = io.StringIO()

    e = P('This is some text')
    e.append('This is some more text')

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is some text') in file_contents
    assert('This is some more text') in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.strip().endswith("</p>")

def test_Head():
    outfile = io.StringIO()

    e = Head('This is some text')
    e.append('This is some more text')

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is some text') in file_contents
    assert('This is some more text') in file_contents

    assert file_contents.startswith("<head>")
    assert file_contents.strip().endswith("</head>")

def test_Title():
    outfile = io.StringIO()

    e = Title('This is some text')
    e.append('This is some more text')

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is some text') in file_contents
    assert('This is some more text') in file_contents

    assert file_contents.startswith("<title>")
    assert file_contents.strip().endswith("</title>")

def test_html_body():
    outfile = io.StringIO()

    e = Html('This is HTML text')
    f = Body('This is BODY text')

    e.append(f)

    e.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is HTML text') in file_contents
    assert('This is BODY text') in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")

def test_step3():
    outfile = io.StringIO()

    p = Html()
    h = Head()
    h.append(Title('This is TITLE'))
    p.append(h)
    b = Body()
    b.append(P('This is P'))
    p.append(b)

    p.render(outfile)

    outfile.seek(0)
    file_contents = outfile.read()

    print(file_contents)

    assert('This is TITLE') in file_contents
    assert('This is P') in file_contents

    assert file_contents.startswith("<html>")
    assert file_contents.strip().endswith("</html>")

