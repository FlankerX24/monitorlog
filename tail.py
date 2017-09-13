#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
import time
from datetime import date
from datetime import datetime

class Tail(object):
    MAX_SLEEP_COUNT = 2
    SINGLE_READ = 5210

    def __init__(self, tailed_file, start=0):
        self.tailed_file       = tailed_file
        self.curr_position     = start
        self.read_callback     = None
        self.sleep_count       = 0

    def follow(self, s=60):
        with open(self.tailed_file) as file_:
            file_.seek(self.curr_position)
            while True:
                if self.sleep_count == Tail.MAX_SLEEP_COUNT:
                    return self.curr_position

                readed = file_.readlines(Tail.SINGLE_READ)
                curr_position = file_.tell()
                if (curr_position - self.curr_position < Tail.SINGLE_READ):
                    time.sleep(s)
                    self.sleep_count += 1
                else:
                    self.sleep_count = 0
                    self.curr_position = curr_position
                    if self.read_callback:
                        self.read_callback(readed)

    def register_read_callback(self, callback):
        self.read_callback = callback

def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def tails(file_pattern, callback):
    start_read = 0
    today = date.today()
    while True:
        file_name = today.strftime(file_pattern)
        print("[%s] start tail file: '%s'" % (now_str(), file_name))
        if today < date.today():
            start_read = 0

        today = date.today()
        try:
            t = Tail(file_name, start_read)
            t.register_read_callback(callback)
            start_read = t.follow()
        except IOError, e:
            print("Error: cannot tail log file: %s, reason: %s" % (file_name, str(e)))
            time.sleep(120)
