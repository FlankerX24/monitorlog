#!/usr/bin/python
# -*- coding: utf-8 -*-

import  sys
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

def send_mail(mailto, subject, content, From="Robot", To="Developer"):
    me = mail_user + "@" + mail_postfix
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(From, 'utf-8')
    msg['To'] = Header(To, 'utf-8')
    msg["Accept-Language"]="zh-CN"
    msg["Accept-Charset"]="ISO-8859-1,utf-8"
    s = smtplib.SMTP()
    s.connect(mail_host, 25)
    s.starttls()
    s.login(mail_user,mail_pass)
    s.sendmail(me, mailto, msg.as_string())
    s.close()
