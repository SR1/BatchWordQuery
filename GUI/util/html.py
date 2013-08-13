#coding=utf-8

import HTMLParser

def HTMLdecode(line):
    return HTMLParser.HTMLParser().unescape(line)
