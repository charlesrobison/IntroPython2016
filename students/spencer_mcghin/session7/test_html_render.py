#!/usr/bin/env python
""" Test code for html_render.py """

import io

from html_render import Body, Element, P


def test_init():
    e = Element()

    e = Element("this is some text")


def test_content():
    e = Element("this is some text")

    assert "this is some text" in e.content


def test_append():
    e = Element("this is some text")

    assert "this is some text" in e.content


def test_render():
    outfile = io.StringIO()

    e = Element("this is some text")

    e.render(outfile, ind=4)

    file_contents = outfile.getvalue()

    print(file_contents)


def test_body_render():
    outfile = io.StringIO()

    b = Body("this is some text")

    b.render(outfile, ind=4)

    file_contents = outfile.getvalue()

    print(file_contents)


def test_p_render():
    outfile = io.StringIO()

    p = P("this is some text")

    p.render(outfile, ind=4)

    file_contents = outfile.getvalue()

    print(file_contents)