# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

##from_addr = raw_input('From: ')
##password = raw_input('Password: ')
##to_addr = raw_input('To: ')
##smtp_server = raw_input('SMTP server: ')
from_addr = "zwm_8086@163.com"
password = "xxxxxx"
to_addr = "zwm_8086@sina.com"
smtp_server = "smtp.163.com"

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()