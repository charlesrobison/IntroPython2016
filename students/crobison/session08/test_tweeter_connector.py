#!/usr/bin/env python3

# Charles Robison
# Term project

from tweeter_connector import connection_confirmation

def test_connection():
    connection_confirmation()
    assert '<twitter.api.Twitter object at 0x103bb1588>'