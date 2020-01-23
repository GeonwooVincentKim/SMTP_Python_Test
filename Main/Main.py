import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


# def sendMail(subject, body):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = "kdsnop@gmail.com"
#     msg['To'] = "kdsnop@naver.com"
#
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.send_message(msg)
#     s.quit()
#
#
# bsObj = BeautifulSoup(urlopen(""))

smtp = smtplib.SMTP('smtp.live.com', 587)
smtp.ehlo()  # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('kdsnop@gmail.com', 'kds0121004!')

msg = MIMEText('본문 테스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = 'kdsnop@gmail.com'
smtp.sendmail('kdsnop@gmail.com', 'kdsnop@naver.com', msg.as_string())

smtp.quit()
