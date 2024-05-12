from email.message import EmailMessage  # Importing EmailMessage class for creating email messages
import ssl  # Importing SSL module for secure connections
import smtplib  # Importing SMTP library for sending emails
from typing import Any  # Importing Any for type hinting

# Importing password from app2 module
try:
    import app2
    password = app2.password
except ImportError:
    password: Any = None  # If app2 or password cannot be imported, set password to None

email_sender = 'email'  # Enter your email address as the sender
email_password = 'password'  # Enter your email's password

email_receiver = ''  # Email address of the recipient

subject = "Don't forget to subscribe"  # Subject of the email
body = """
When you watch a video, please hit subscribe
"""  # Body of the email

em = EmailMessage()  # Creating an EmailMessage object
em['From'] = email_sender  # Setting sender's email address
em['To'] = email_receiver  # Setting recipient's email address
em['Subject'] = subject  # Setting email subject
em.set_content(body)  # Setting email body

context = ssl.create_default_context()  # Creating SSL context for secure connection

# Establishing a connection to the SMTP server and sending the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)  # Logging in to the SMTP server
    smtp.sendmail(email_sender, email_receiver, em.as_string())  # Sending the email
