import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Open a file: file
file = open('mailtext.txt',mode='r')

# read all lines at once
mail_content = file.read()

# close the file
file.close()

#The mail addresses and password
sender_address = 'tanzila@anchorblock.vc'
sender_pass = 'XXXXXXXXXXXXXX'
receiver_address = 'tanzzilaalam@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')


