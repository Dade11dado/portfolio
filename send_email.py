import smtplib as sp
import ssl

host = "smtp.gmail.com"
port = 465

password = "btzteiannvmicpft"
username = "davidevavassoriprova@gmail.com"
receiver = "davide.vavassori@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Hello!
How are you? By BY"""

with sp.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver, message)

