import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "sajjadnetworker2015@gmail.com"
password = "ecng ttje iucu uizj"

receiver = "sajjadnetworker2015@gmail.com"
message = """\
Subject: Hi !
how are you ?
bye!
"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
    