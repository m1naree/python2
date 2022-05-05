from email import message
import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message= EmailMessage()
message.set_content("안녕하세요 지혜민입니다.")
def sendEmail(addr):
    reg="^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 발송되었습니다.")
    else:
        print("유효한 Email 주소가 아닙니다.")


message["Subject"]  ="안녕하세요 지혜민 과제4 메일입니다."
message["From"] = "sunsun072140@gmail.com"
message["To"] = "ksjoon28@naver.com"

smtp= smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("sunsun072140@gmail.com","#Gpals990721")
smtp.send_message(message)
sendEmail("ksjoon28@naver.com")
smtp.quit()