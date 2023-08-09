import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
# from dotenv import load_dotenv

# load_dotenv()
from flask import Flask, request
app = Flask(__name__)

# Sender's Gmail credentials
sender_email = os.getenv('sender_email')
app_password = os.getenv('app_password')

# Recipient email
def genEmail(commitMessage,commitLink):
    generatedEmail = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>

    <head>
        <!-- Compiled with Bootstrap Email version: 1.4.0 -->
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <meta name="x-apple-disable-message-reformatting">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
        <style type="text/css">
            body,
            table,
            td {
                font-family: Helvetica, Arial, sans-serif !important
            }

            .ExternalClass {
                width: 100%
            }

            .ExternalClass,
            .ExternalClass p,
            .ExternalClass span,
            .ExternalClass font,
            .ExternalClass td,
            .ExternalClass div {
                line-height: 150%
            }

            a {
                text-decoration: none
            }

            * {
                color: inherit
            }

            a[x-apple-data-detectors],
            u+#body a,
            #MessageViewBody a {
                color: inherit;
                text-decoration: none;
                font-size: inherit;
                font-family: inherit;
                font-weight: inherit;
                line-height: inherit
            }

            img {
                -ms-interpolation-mode: bicubic
            }

            table:not([class^=s-]) {
                font-family: Helvetica, Arial, sans-serif;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                border-spacing: 0px;
                border-collapse: collapse
            }

            table:not([class^=s-]) td {
                border-spacing: 0px;
                border-collapse: collapse
            }

            @media screen and (max-width: 600px) {

                .max-w-56,
                .max-w-56>tbody>tr>td {
                    max-width: 224px !important;
                    width: 100% !important
                }

                .max-w-96,
                .max-w-96>tbody>tr>td {
                    max-width: 384px !important;
                    width: 100% !important
                }

                .w-lg-80,
                .w-lg-80>tbody>tr>td {
                    width: auto !important
                }

                .w-full,
                .w-full>tbody>tr>td {
                    width: 100% !important
                }

                .w-32,
                .w-32>tbody>tr>td {
                    width: 128px !important
                }

                .pt-4:not(table),
                .pt-4:not(.btn)>tbody>tr>td,
                .pt-4.btn td a,
                .py-4:not(table),
                .py-4:not(.btn)>tbody>tr>td,
                .py-4.btn td a {
                    padding-top: 16px !important
                }

                .pb-4:not(table),
                .pb-4:not(.btn)>tbody>tr>td,
                .pb-4.btn td a,
                .py-4:not(table),
                .py-4:not(.btn)>tbody>tr>td,
                .py-4.btn td a {
                    padding-bottom: 16px !important
                }

                *[class*=s-lg-]>tbody>tr>td {
                    font-size: 0 !important;
                    line-height: 0 !important;
                    height: 0 !important
                }

                .s-6>tbody>tr>td {
                    font-size: 24px !important;
                    line-height: 24px !important;
                    height: 24px !important
                }

                .s-10>tbody>tr>td {
                    font-size: 40px !important;
                    line-height: 40px !important;
                    height: 40px !important
                }
            }
        </style>
    </head>

    <body
        style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;"
        bgcolor="#ffffff">
        <table class="body" valign="top" role="presentation" border="0" cellpadding="0" cellspacing="0"
            style="outline: 0; width: 100%; min-width: 100%; height: 100%; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family: Helvetica, Arial, sans-serif; line-height: 24px; font-weight: normal; font-size: 16px; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; color: #000000; margin: 0; padding: 0; border-width: 0;"
            bgcolor="#ffffff">
            <tbody>
                <tr>
                    <td valign="top" style="line-height: 24px; font-size: 16px; margin: 0;" align="left">
                        <table class="bg-black w-full" role="presentation" border="0" cellpadding="0" cellspacing="0"
                            style="width: 100%;" bgcolor="#000000" width="100%">
                            <tbody>
                                <tr>
                                    <td style="line-height: 24px; font-size: 16px; width: 100%; margin: 0;" align="left"
                                        bgcolor="#000000" width="100%">
                                        <table class="container" role="presentation" border="0" cellpadding="0"
                                            cellspacing="0" style="width: 100%;">
                                            <tbody>
                                                <tr>
                                                    <td align="center"
                                                        style="line-height: 24px; font-size: 16px; margin: 0; padding: 0 16px;">
                                                        <!--[if (gte mso 9)|(IE)]>
                                  <table align="center" role="presentation">
                                    <tbody>
                                      <tr>
                                        <td width="600">
                                <![endif]-->
                                                        <table align="center" role="presentation" border="0" cellpadding="0"
                                                            cellspacing="0"
                                                            style="width: 100%; max-width: 600px; margin: 0 auto;">
                                                            <tbody>
                                                                <tr>
                                                                    <td style="line-height: 24px; font-size: 16px; margin: 0;"
                                                                        align="left">
                                                                        <table class="s-10 w-full" role="presentation"
                                                                            border="0" cellpadding="0" cellspacing="0"
                                                                            style="width: 100%;" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;"
                                                                                        align="left" width="100%"
                                                                                        height="40">
                                                                                        &#160;
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="ax-center" role="presentation"
                                                                            align="center" border="0" cellpadding="0"
                                                                            cellspacing="0" style="margin: 0 auto;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 24px; font-size: 16px; margin: 0;"
                                                                                        align="left">
                                                                                        <img class="w-32"
                                                                                            src="https://iconsplace.com/wp-content/uploads/_icons/ffffff/256/png/github-icon-18-256.png"
                                                                                            style="height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; width: 128px; border-style: none; border-width: 0;"
                                                                                            width="128">
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="s-10 w-full" role="presentation"
                                                                            border="0" cellpadding="0" cellspacing="0"
                                                                            style="width: 100%;" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;"
                                                                                        align="left" width="100%"
                                                                                        height="40">
                                                                                        &#160;
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="ax-center" role="presentation"
                                                                            align="center" border="0" cellpadding="0"
                                                                            cellspacing="0" style="margin: 0 auto;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 24px; font-size: 16px; margin: 0;"
                                                                                        align="left">
                                                                                        <h1 class="text-white text-center"
                                                                                            style="color: #ffffff; padding-top: 0; padding-bottom: 0; font-weight: 500; vertical-align: baseline; font-size: 36px; line-height: 43.2px; margin: 0;"
                                                                                            align="center">{commitMessage}
                                                                                        </h1>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="s-10 w-full" role="presentation"
                                                                            border="0" cellpadding="0" cellspacing="0"
                                                                            style="width: 100%;" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;"
                                                                                        align="left" width="100%"
                                                                                        height="40">
                                                                                        &#160;
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="ax-center" role="presentation"
                                                                            align="center" border="0" cellpadding="0"
                                                                            cellspacing="0" style="margin: 0 auto;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 24px; font-size: 16px; margin: 0;"
                                                                                        align="left">
                                                                                        <img class="max-w-56  rounded-full"
                                                                                            src="https://github.com/prabincankod.png"
                                                                                            style="height: auto; line-height: 100%; outline: none; text-decoration: none; display: block; border-radius: 9999px; max-width: 224px; width: 100%; border-style: none; border-width: 0;"
                                                                                            width="224">
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="s-10 w-full" role="presentation"
                                                                            border="0" cellpadding="0" cellspacing="0"
                                                                            style="width: 100%;" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;"
                                                                                        align="left" width="100%"
                                                                                        height="40">
                                                                                        &#160;
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="ax-center" role="presentation"
                                                                            align="center" border="0" cellpadding="0"
                                                                            cellspacing="0" style="margin: 0 auto;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 24px; font-size: 16px; margin: 0;"
                                                                                        align="left">
                                                                                        <p class="max-w-96 lh-lg text-white text-center text-2xl"
                                                                                            style="line-height: 2; font-size: 24px; color: #ffffff; max-width: 384px; -premailer-width: 384; width: 100%; margin: 0;"
                                                                                            align="center">
                                                                                            This is an auto-generated email
                                                                                            which means I have submitted the
                                                                                            assignment or I made a commit
                                                                                            push.
                                                                                        </p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="s-10 w-full" role="presentation"
                                                                            border="0" cellpadding="0" cellspacing="0"
                                                                            style="width: 100%;" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;"
                                                                                        align="left" width="100%"
                                                                                        height="40">
                                                                                        &#160;
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table
                                                                            class="btn btn-yellow-300 rounded-full fw-800 text-5xl py-4 ax-center  w-full w-lg-80"
                                                                            role="presentation" align="center" border="0"
                                                                            cellpadding="0" cellspacing="0"
                                                                            style="border-radius: 9999px; border-collapse: separate !important; width: 320px; font-size: 48px; line-height: 57.6px; font-weight: 800 !important; margin: 0 auto;"
                                                                            width="320">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 24px; font-size: 16px; border-radius: 9999px; width: 320px; font-weight: 800 !important; margin: 0;"
                                                                                        align="center" bgcolor="#ffda6a"
                                                                                        width="320">
                                                                                        <a href="{commitLink}"
                                                                                            style="color: #111111; font-size: 16px; font-family: Helvetica, Arial, sans-serif; text-decoration: none; border-radius: 9999px; line-height: 20px; display: block; font-weight: 800 !important; white-space: nowrap; background-color: #ffda6a; padding: 16px 12px; border: 1px solid #ffda6a;">Commit
                                                                                            Details</a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                        <table class="s-10 w-full" role="presentation"
                                                                            border="0" cellpadding="0" cellspacing="0"
                                                                            style="width: 100%;" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td style="line-height: 40px; font-size: 40px; width: 100%; height: 40px; margin: 0;"
                                                                                        align="left" width="100%"
                                                                                        height="40">
                                                                                        &#160;
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if (gte mso 9)|(IE)]>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                                <![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0"
                            style="width: 100%;" width="100%">
                            <tbody>
                                <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;"
                                        align="left" width="100%" height="24">
                                        &#160;
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="text-muted text-center" style="color: #718096;" align="center">
                            <code>
                                Sent with &#10084;&#65039; from <a href="https://github.com/prabincankod/flasksendmessage"
                                    style="color: #0d6efd;">flasksendmessage</a> by <a
                                    href="https://github.com/prabincankod%20" style="color: #0d6efd;">@prabincankod </a>
                            </code>
                        </div>
                        <table class="s-6 w-full" role="presentation" border="0" cellpadding="0" cellspacing="0"
                            style="width: 100%;" width="100%">
                            <tbody>
                                <tr>
                                    <td style="line-height: 24px; font-size: 24px; width: 100%; height: 24px; margin: 0;"
                                        align="left" width="100%" height="24">
                                        &#160;
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </body>

    </html>'''
    newEmail = generatedEmail.replace("{commitLink}", commitLink)
    newEmail = newEmail.replace("{commitMessage}", commitMessage)
    return newEmail

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
