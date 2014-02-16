#http://www.maprantala.com/2010/07/09/python-emailer/
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'node.dangles AT gmail.com'
password = 'myFancyPassword'
smtpaddr = 'smtp.gmail.com'
smtpport = 587

def SendMess(toadd, subject, body):

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toadd
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

text = msg.as_string()

server = smtplib.SMTP(smtpaddr, smtpport)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, password)

server.sendmail(fromaddr, toadd, text)