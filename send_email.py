import smtplib
import ssl

username = 'davoudpour2000@gmail.com'
password = 'sqaqsjjhdsdnqwbt'
host = 'smtp.gmail.com'
port = 465
context = ssl.create_default_context()
receiver = 'davoudpour2000@gmail.com'


def send_email(message):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


