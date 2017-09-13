#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from tail import tails
from errmailcb import callback
from errmailcb import send_mail
import sys

def main():
    if len(sys.argv) >= 2:
        file_pattern = sys.argv[1]
        subject      = sys.argv[2]
    else:
        file_pattern = "./game.%Y%m%d.log"
        subject      = "服务器日志报错"

    send_mail.subject = subject
    tails(file_pattern, callback)

if __name__ == "__main__":
    main()
