#attachement
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders


SUBJECT = "Email Data"

msg = MIMEMultipart()
msg['Subject'] = SUBJECT 
msg['From'] = self.EMAIL_FROM
msg['To'] = ', '.join(self.EMAIL_TO)

part = MIMEBase('application', "octet-stream")
part.set_payload(open("text.txt", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="text.txt"')

msg.attach(part)

server = smtplib.SMTP(self.EMAIL_SERVER)
server.sendmail(self.EMAIL_FROM, self.EMAIL_TO, msg.as_string())