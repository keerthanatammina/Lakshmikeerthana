import smtplib#simple mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText #mime- multi purpose internet mail extension

#defining data
email_user="sepjune0306@gmail.com"
email_sender="anurupa070@gmail.com"
subject="nee nduku"
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_sender
msg['Subject']=subject
body="biryani tintava"
msg.attach(MIMEText(body,'plain'))
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("sepjune0306@gmail.com","esufqabdmobzqsdg")
server.sendmail(email_user,email_sender,text)



