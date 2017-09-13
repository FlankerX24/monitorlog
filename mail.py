#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import  smtplib
from    email.mime.text import MIMEText
from    email.header import Header

reload(sys)
sys.setdefaultencoding('utf8')

#发送者
mail_host       = "smtp.qq.com"
mail_user       = "user@example.com"
mail_pass       = "passwd" #ssl认证
mail_postfix    = "qq.com"

def send_mail(mailto, subject, content):
    me = mail_user + "@" + mail_postfix
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header("Robot", 'utf-8')
    msg['To'] = Header("Developer", 'utf-8')
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    s = smtplib.SMTP()
    s.connect(mail_host, 25)
    s.starttls()
    s.login(mail_user,mail_pass)
    s.sendmail(me, mailto, msg.as_string())
    s.close()

def main():
    send_mail(["user@example.com"], "项目日志报警", "文件名：报警如下")
    pass

if __name__ == "__main__":
    main()
