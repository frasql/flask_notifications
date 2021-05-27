import re
import os
from werkzeug.security import generate_password_hash, check_password_hash
from numbers import Number
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime



class Utils(object):
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_pattern = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_pattern.match(email) else False 

    @staticmethod
    def hash_password(password: str) -> str:
        return generate_password_hash(password)

    @staticmethod
    def check_hashed_password(password: str, hashed_password: str) -> bool:
        return check_password_hash(password, hashed_password)
    
    @staticmethod
    def replace_not_ascii(value: str) -> str:
        return re.sub(r'[^\x00-\x7F]+','-', value)
    
    # validate an username on input
    @staticmethod
    def username_is_valid(username: str) -> str:
        if username is None or username == "":
            raise ValueError("Devi inserire un username")
        if isinstance(username, Number):
            raise ValueError("Devi inserire una stringa non un numero!!!!")
        # ---- username rules ---#
        return True
    
    @staticmethod
    def string_to_datetime(str_datetime, format="%Y-%m-%dT%H:%M"):
        return datetime.datetime.strptime(str_datetime, format)
    
    @staticmethod
    def datetime_to_string(datetime_obj, format="%Y-%m-%dT%H:%M"):
            return datetime.datetime.strftime(datetime_obj, format)



username = os.getenv('MAIL_USER')
password = os.getenv('MAIL_PASSWORD')

# send mail to single/multiple user/s
def send_mail(text: str ='Email Body', subject: str = 'Hello', from_email: str ='Name <address>', to_emails=None, html=None) -> None:
    assert isinstance(to_emails, list)

    # create message
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] =  ','.join(to_emails)
    msg['Subject'] = subject

    # attach text
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    
    # attach html
    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)
    # login to smtp server
    with smtplib.SMTP(host='smtp.domain.com', port=587) as server:
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_emails, msg)
