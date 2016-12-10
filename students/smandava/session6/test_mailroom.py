"""Nov 27th, 2016 Test cases for Mailroom exercise."""

from sm_mailroom_refactor import print_report, send_thanks, write_letter
import io
import os.path

def test_printreport():
    result = print_report()
    print(result)
    assert 'Alfred Hitchcock 60 3 20' in result
    assert 'Martin Scorsese 90 3 30' in result
    assert 'Ridley Scott 70 4 17.5' in result
    assert 'Steven Spielberg 100 4 25' in result


def test_sendthanks_list():
    result = send_thanks('list')
    print(result)
    assert 'Alfred Hitchcock' in result
    assert 'Martin Scorsese' in result
    assert 'Ridley Scott' in result
    assert 'Steven Spielberg' in result

def test_sendthanks_add_donation():
    result = send_thanks('Steven Spielberg', 60)
    print(result)
    assert ('Steven Spielberg', [40, 20, 30, 10, 60]) == result

def test_sendthanks_non_numeric_donation():
    result = send_thanks('Ridley Scott', 'abc')
    print(result)
    assert 'ValueError' == result

def test_sendthanks_new_donor():
    result = send_thanks('Sasi Mandava', 50)
    print(result)
    assert ('Sasi Mandava', [50]) == result

def test_sendthanks_new_donor_non_numeric_donation():
    result = send_thanks('Sasi Mandava', 'abc')
    print(result)
    assert 'ValueError' == result

def test_writeletter():
    result = write_letter()
    assert "Created Thank you letter!" == result

def test_writeletter_exists():
    assert os.path.isfile('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_Steven Spielberg.txt') is True
    assert os.path.isfile('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_Ridley Scott.txt') is True
    assert os.path.isfile('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_Martin Scorsese.txt') is True


def test_writeletter_contents():
    assert ("Thank you very much for your generous donation" in io.open('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_Francis Coppola.txt').read()) is True
    assert ("Thank you very much for your generous donation" in io.open('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_Ridley Scott.txt').read()) is True
    assert ("Thank you very much for your generous donation" in io.open('/Users/Mandava/Documents/python/IntroPython2016/students/smandava/session6/thankyouletter_Steven Spielberg.txt').read()) is True
