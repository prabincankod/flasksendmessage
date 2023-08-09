import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from flask import Flask, request
from emailgen import genEmail
app = Flask(__name__)

# Sender's Gmail credentials
sender_email = os.getenv('sender_email')
app_password = os.getenv('app_password')
# Sender's Gmail credentials
recipient_email = os.getenv('recipient_email')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get-hook', methods=['POST', 'GET'])
def get_hook():
    if request.method == 'POST':
        eventType = request.headers["X-GitHub-Event"]
        if eventType == "ping":
            return "pingedddd"
        else:
            json = request.json
            commitMessage = json["head_commit"]["message"]
            commitLink= json["head_commit"]["url"]
            # Create the MIME object
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = f"Prabin Subedi's {commitMessage} "

            # Email content
            # body = f'commit from : {json["head_commit"]["url"]}'
            body = genEmail(commitMessage,commitLink)
            message.attach(MIMEText(body, "html"))
            # Establish a secure connection with Gmail's SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, recipient_email,
                                message.as_string())

            return commitMessage
    return 'Hello, World!'
