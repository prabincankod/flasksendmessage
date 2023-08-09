import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask, request
app = Flask(__name__)

# Sender's Gmail credentials
sender_email = os.getenv('sender_email')
app_password = os.getenv('app_password')

# Recipient email



@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get-hook', methods=['POST', 'GET'])
def get_hook():
    recipient_email = os.getenv('recipient_email')
    if request.method == 'POST':
        eventType = request.headers["X-GitHub-Event"]
        if eventType == "ping":
            return "pingedddd"
        else:
            json = request.json
            commitMessage = json["head_commit"]["message"]
            # Create the MIME object
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = f"Prabin Subedi's {commitMessage} "

            # Email content
            body = f'commit from : {json["head_commit"]["url"]}'
            message.attach(MIMEText(body, "plain"))
            # Establish a secure connection with Gmail's SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, recipient_email,
                                message.as_string())

            return commitMessage
    return 'Hello, World!'
