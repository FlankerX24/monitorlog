#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
import re
import mail

ERROR_PATTERN = re.compile(r'\[:\w{8}\] lua call \[\w+ to :\w+ : \w+ msgsz = \d+\] error : ')
NORMAL_PATTERN = re.compile(r'\[:\w{8}\]')

def find_lua_error(readed):
    lines = []
    for line in readed:
        if not NORMAL_PATTERN.match(line):
            find_lua_error.cache.append(line)
        else:
            if find_lua_error.cache:
                lines.append("".join(find_lua_error.cache))
                find_lua_error.cache = []

            if ERROR_PATTERN.match(line):
                find_lua_error.cache.append(line)

    return lines

find_lua_error.cache = []

def gen_read_callback(find_callback):
    def _callback(readed):
        content = find_lua_error(readed)
        content = [x for x in content if x.strip()]
        if len(content) > 0:
            find_callback(content)

    return _callback

def send_mail(content):
    for errorLog in content:
        try:
            mail.send_mail(["user@example.com"], send_mail.subject, errorLog)
        except Exception, e:
            print("Error: cannot send email: ", e)

callback = gen_read_callback(send_mail)
