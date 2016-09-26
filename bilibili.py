import urllib
import urllib2
import re
import smtplib
import httplib
import time
from email.mime.text import MIMEText
import os
import sys

#防止出现连接不上的情况
#httplib.HTTPConnection._http_vsn = 10
#httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

while(True):
  _user="发送方邮箱"
  _pwd="IMAP/SMTP授权码，需要在邮箱设置中开启"
  _to="接受方邮箱"

  msg = MIMEText("XXXX")
  msg["Subject"]="XXXX~"
  msg["From"]="XXXX"
  msg["To"]="XXX"


  url = 'http://live.bilibili.com/live/getInfo?roomid=主播的房间号'
  user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
  headers = { 'User-Agent' : user_agent }
  request = urllib2.Request(url,headers = headers)
  response = urllib2.urlopen(request)
  #print response.read()
  if re.findall("on",response.read()):
    s=smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print True
    #os.system('shutdown -s -f -t 0')，可以设置主播上线之后关机
    break
  else:
    print False
    time.sleep(3)  