import smtplib
from email.mime.text import MIMEText
import imaplib
import email
from email.header import decode_header

import sys

# Sending an email
def send_email(subject, message, from_email, to_email):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    domain = from_email.split('@')[1]
    domain = domain.split('.')[0]

    smtp_servers = {
        "aol": {
            "address": "smtp.aol.com"
        }
    }

    if len( sys.argv ) < 2:
        print("Please provide a password");
        return;

    password = sys.argv[1];

    if domain == 'aol':
        print("Connecting to server")
        server = smtplib.SMTP_SSL(smtp_servers['aol']['address'], 465)
        print("Logging in")
        server.login(from_email, password)
        print("Sending message...")
        server.send_message(msg)
        server.quit()


send_email("Hi", "Hi", "luyang.l@aol.com", "lucas.liu@wexinc.com");
