import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

email_user="sepjune0306@gmail.com"
email_pwd="esufqabdmobzqsdg"
email_sender="anurupa070@gmail.com"
subject="invitation"
text="please come and join with us for our baby shower"
attach="My Invitation (1).jpeg"
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_sender
msg['Subject']=subject
msg.attach(MIMEText(text))
part=MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment;filename="%s"' %os.path.basename(attach))
msg.attach(part)
mailServer=smtplib.SMTP('smtp.gmail.com',587)
mailServer.starttls()
mailServer.login(email_user,email_pwd)
mailServer.sendmail(email_user,email_sender,msg.as_string())
mailServer.close()



#send multiple emails with same subject(pandas) read email data from excel files
#find_all
#ms excel

