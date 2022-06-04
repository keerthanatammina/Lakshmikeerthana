import smtplib
print(dir(smtplib))
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #tls-transport layer

#next loginto the server
server.login("sepjune0306@gmail.com","esufqabdmobzqsdg")#give your gmail user name and password

#send the email
msg="C:/Users/LAKSHMI/Downloads/My Invitation (1).jpeg"

#message from the headers
server.sendmail("sepjune0306@gmail.com","tejasrilaki999@gmail.com",msg)

