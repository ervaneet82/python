import smtplib


fromaddr = 'ervaneet82@gmail.com'
toaddrs  = 'ervaneet82@gmail.com'
msg = """From: ervaneet82@gmail.com
Subject: Welcome
Hello, this is doge.
"""

#Change according to your settings
smtp_server = 'email-smtp.us-east-1.amazonaws.com'
smtp_username = 'AKIAUB72HZT2QIAEB55V'
smtp_password = 'BMuPkvSRupwjJaieTcLhbh/NJmvYtK6ssMHWfq2vJSRa'
smtp_port = '587'
smtp_do_tls = True

server = smtplib.SMTP(
    host = smtp_server,
    port = smtp_port,
    timeout = 10
)

server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()