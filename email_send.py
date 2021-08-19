import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


email_user='sendzip3@gmail.com'
#email_send=input('Input Email Id to send the files to')
def mail_user(email_id):
    subject = 'Mashup Zipped files in Python'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_id
    msg['Subject'] = subject
    body='Hi there, sending this email from Python to send the mashup of Songs.'

    msg.attach(MIMEText(body,'plain'))

    #filename='resized_dir_zip.zip'
    attachment  =open('songs.zip','rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+'songs.zip')

    msg.attach(part)
    text = msg.as_string()



    server=smtplib.SMTP('smtp.gmail.com',587) #gmail server and port number
    server.starttls()#secure connections
    server.login(email_user,'sendzip112903')


    server.sendmail(email_user,email_id,text)
    server.quit()
