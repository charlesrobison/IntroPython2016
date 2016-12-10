"""
Name: Paul Briant
Date: 11/15/16
Class: Introduction to Python
Session: 07
Assignment: HTML Renderer

Description:
Tests for HTML Renderer
"""

# -------------------------------Imports----------------------------------------
import html_render as hr
import io

# -------------------------------Functions--------------------------------------


def test_init():
    e = hr.Element()
    e = hr.Element("Please remain calm, this is a test.")


def test_two_instances():
    e = hr.Element("Testing, 1 2 3..")
    e2 = hr.Element("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    assert "More tests! We need more tests!" not in e2.content


def test_render():
    """
    Tests whether render successfully writes content to file by creating
    instance of element, adding content to it using the append function and
    calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = hr.Element("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    e.render(output, "    ")
    file_cont = output.getvalue()
    assert("Testing, 1 2 3..") in file_cont
    assert("More tests! We need more tests!") in file_cont
    assert file_cont.strip().startswith("<html>")
    assert file_cont.strip().endswith("</html>")
    # Verify there is indentation
    assert file_cont.startswith("    ")


def test_html_render():
    """
    Tests whether render successfully writes content to file for the html tag
    by creating instance of HTML, adding content to it using the append
    function and calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = hr.Html("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    e.render(output, "    ")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith("<html>")
    assert file_cont.strip().endswith("</html>")
    # Verify amount of indentation
    assert file_cont.startswith("    ")


def test_body_render():
    """
    Tests whether render successfully writes content to file for the body tag
    by creating instance of Body, adding content to it using the append
    function and calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = hr.Body("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    e.render(output, "    ")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith("<body>")
    assert file_cont.strip().endswith("</body>")
    # Verify amount of indentation
    assert file_cont.startswith("    ")


def test_text_wrapper():
    """
    Verify that text based content is produced.
    """
    output = io.StringIO()
    tw = hr.TextWrapper("More tests! We need more tests!")
    tw.render(output, "")
    file_cont = output.getvalue()
    assert file_cont == "More tests! We need more tests!"


def test_p_render():
    """
    Tests whether render successfully writes content to file for the p tag
    by creating instance of P, adding content to it using the append
    function and calling the render funtion on it.
    """
    # Creates in memory version of content to write to file
    output = io.StringIO()
    e = hr.P("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    e.render(output, "    ")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith("<p>")
    assert file_cont.strip().endswith("</p>")
    # Verify amount of indentation
    assert file_cont.startswith("    ")


def test_append_instances():
    """
    Test to verify an instance of an html element can be appended into another.
    """
    output = io.StringIO()
    e_body = hr.Body()
    e_p = hr.P("Testing, 1 2 3..")
    e_body.append(e_p)
    e_body.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.startswith("<body>")
    assert file_cont.strip().endswith("</body>")
    print(file_cont)
    assert "Testing, 1 2 3.." in file_cont
    # check p tag is in body
    assert "<p>" in file_cont and "</p>" in file_cont
    # additional tests?


def test_head_render():
    """
    Tests whether render successfully writes content to file for the head tag
    by creating instance of Head, adding content to it using the append
    function and calling the render funtion on it.
    """
    output = io.StringIO()
    e = hr.Head("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    e.render(output, "    ")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith("<head>")
    assert file_cont.strip().endswith("</head>")
    # Verify amount of indentation
    assert file_cont.startswith("    ")


def test_onelinetag_title():
    """
    Tests whether the element subclass of onelinetag successfully writes all
    content on the same line to  a file for the inline tag 'title'. This is
    tested by creating an instance of Title, adding content to it using the
    append function and calling the render funtion on it.
    """
    output = io.StringIO()
    e = hr.Title("Testing, 1 2 3..")
    e.append("More tests! We need more tests!")
    e.render(output, "    ")
    file_cont = output.getvalue()
    assert "\n" not in file_cont[:-2]
    assert file_cont.strip().startswith("<title>")
    assert file_cont.strip().endswith("</title>")
    # Verify amount of indentation
    assert file_cont.startswith("    ")


def test_element_attributes():
    """
    Verifies that attributes have been correctly implemented in output file.
    """
    output = io.StringIO()
    e = hr.P("Testing, 1 2 3..", id="test", style="line-height:200%")
    e.render(output, "")
    file_cont = output.getvalue()
    print(file_cont)
    assert 'id="test"' in file_cont
    assert 'style="line-height:200%"' in file_cont


def test_selfclosingtag_hr():
    """
    Verifies that the self closing tag hr is one line and outputed correctly.
    """
    output = io.StringIO()
    e = hr.Hr()
    e.render(output, "")
    file_cont = output.getvalue()
    assert "\n" not in file_cont[:-2]
    assert file_cont == "<hr />"


def test_br_in_p():
    """
    Test the creation f the br tag within the p tag.
    """
    output = io.StringIO()
    p = hr.P("Testing, 1 2 3..")
    p.append(hr.Br())
    p.append("More tests! We need more tests!")
    p.render(output, "")

    file_cont = output.getvalue().split('\n')
    print(file_cont)
    assert file_cont[2].strip() == "<br />"


def test_selfclosingtag_br():
    """
    Verifies that the self closing tag br is one line and outputed correctly.
    """
    output = io.StringIO()
    e = hr.Br()
    e.render(output, "")
    file_cont = output.getvalue()
    assert "\n" not in file_cont[:-2]
    assert file_cont == "<br />"


def test_a():
    """
    Verify the link tag displays the link and content accordingly.
    """
    output = io.StringIO()
    a = hr.A("http://google.com", "link to google")
    a.render(output, "")
    file_cont = output.getvalue()
    assert "link to google" in file_cont
    assert file_cont.strip().startswith('<a href="http://google.com">')
    assert file_cont.strip().endswith('</a>')


def test_ul():
    """
    Verify ul tag is displayed correctly.
    """
    output = io.StringIO()
    ul = hr.Ul("Testing, 1 2 3..", style="line-height:200%", id="TheList")
    ul.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith('<ul')
    assert 'style="line-height:200%"' in file_cont
    assert 'id="TheList"' in file_cont
    assert file_cont.strip().endswith('</ul>')


def test_li():
    """
    Verify li tag is displayed correctly.
    """
    output = io.StringIO()
    ul = hr.Li("Testing, 1 2 3..", style="color: green")
    ul.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith('<li style="color: green">')
    assert file_cont.strip().endswith('</li>')


def test_list():
    """
    Verify li tags are correctly appended into ul tags.
    """
    output = io.StringIO()
    ul = hr.Ul()
    li1 = hr.Li("Testing, 1 2 3..", style="color: blue")
    li2 = hr.Li("More tests! We need more tests!")
    ul.append(li1)
    ul.append(li2)
    ul.render(output, "")
    file_cont = output.getvalue()
    print(file_cont)
    assert '<li style="color: blue">' in file_cont
    assert "More tests! We need more tests!" in file_cont
    assert file_cont.strip().endswith('</ul>')


def test_header():
    """
    Verify header tag was created correctly
    """
    output = io.StringIO()
    h1 = hr.H(1, "More tests! We need more tests!")
    h1.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith("<h1>")
    assert file_cont.strip().endswith("</h1>")
    assert "More tests! We need more tests!" in file_cont


def test_doctype():
    """
    Test the html subclass to ensure the Doctype is above the opening html tag.
    """
    output = io.StringIO()
    html = hr.Html()
    html.render(output, "")
    file_cont = output.getvalue()
    assert file_cont.strip().startswith("<!DOCTYPE html>")


def test_meta():
    """
    Verify meta tag was created correctly
    """
    output = io.StringIO()
    meta = hr.Meta(charset="UTF-8")
    meta.render(output, "")
    file_cont = output.getvalue()
    assert "\n" not in file_cont[:-2]
    assert '<meta charset="UTF-8" />' == file_cont
