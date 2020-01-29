## start SMTP server 
## python -m smtpd -c DebuggingServer -n localhost:1025
## If you are using gmail. You may need to loosen security by going to
## https://www.google.com/settings/security/lesssecureapps

import smtplib, ssl
import getpass
port = 465
psw = input("amd123")
ctx = ssl.create_default_context()
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "tirumalareddy@gmail.com"
receiver_email="mtreddy@hotmail.com"
paswd=getpass.getpass()

server = smtplib.SMTP(smtp_server,port)
server.login(sender_email, pswd)
server.ehlo()
server.starttls(context=ctx)
server.ehlo()
## To send email
## msg=""" Subject = Hi There This message sent using python"""
##server.sendmail(sender_email, receiver_email, msg)
