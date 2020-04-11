import smtplib
from email.mime.text import MIMEText
import time


def Menu():
    print("Do you want to send E-Mail??")
    select_menu = input("1. Yes  2. No ")
    select_list = []

    while True:
        print("Hold on Please...")
        time.sleep(2)
        if select_menu is '1':
            Email = sendMail()
            select_list.append(Email)
            break

        elif select_menu is '2':
            print("Thank you for Using this Application")
            exit(0)
            break

        else:
            print("There is no Manual Related to : {}".format(select_menu))


def sendMail():
    ID, PWD = input("Enter your email address and password. : \n").split()
    time.sleep(1)

    Receiver = input("Enter the email address of the person receiving the email. : \n")
    time.sleep(1)

    print("When writing an email, use _ instead of spaces. \nFor the Example, How_Are_You_Doing?")
    Subject, Body = input("Please enter the subject and content of the email. : \n").split()
    time.sleep(1)

    smtp = smtplib.SMTP('smtp.live.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(ID, PWD)

    msg = MIMEText(Body)
    msg['Subject'] = Subject
    msg['From'] = ID
    msg['To'] = Receiver
    smtp.sendmail(ID, Receiver, msg.as_string())
    print("Success for Sent Email")
    smtp.quit()


Menu()

