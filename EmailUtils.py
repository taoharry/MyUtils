#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import smtplib
from email.mime.text import MIMEText

from config.config import mail_host,mail_user,mail_pass


def send_mail(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP_SSL()
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()

    except (Exception):
        print("失败咯...")

if __name__ == '__main__':
    table = """<table border="1">
        <tr>
        <td>row 1, cell 1</td>
        <td>row 1, cell 2</td>
        </tr>
        <tr>
        <td>row 2, cell 1</td>
        <td>row 2, cell 2</td>
        </tr>
        </table>"""
    send_mail("916414005@qq.com","hello",table)

