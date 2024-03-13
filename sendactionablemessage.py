#! /usr/local/bin/python
"""Sends an actionable message to yourself
Usage: 'sendactionablemessage.py -u <username> -p <password>'
"""

import sys
import getopt
from smtplib import SMTP as SMTP
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587

HTML_CONTENT = """\
<html>
<head>
    <script type="application/ld+json">{
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "originator": "",
    "themeColor": "E81123",
    "sections": [
        {
            "heroImage": {
                "image": "http://messagecardplayground.azurewebsites.net/assets/TINYPulseEngageBanner.png"
            }
        },
        {
            "startGroup": true,
            "activityImage": "http://messagecardplayground.azurewebsites.net/assets/TINYPulseQuestionIcon.png",
            "activityImageStyle": "normal",
            "activityTitle": "**What do you love about your job?**",
            "activityText": "It can be nothing, everything, and anything in between. Sharing is caring.",
            "potentialAction": [
                {
                    "@type": "ActionCard",
                    "name": "Yes",
                    "inputs": [
                        {
                            "@type": "TextInput",
                            "id": "comment",
                            "isMultiline": true,
                            "title": "Feel free to elaborate"
                        }
                    ],
                    "actions": [
                        {
                            "@type": "HttpPOST",
                            "name": "Answer anonymously",
                            "isPrimary": true,
                            "target": "http://..."
                        }
                    ]
                }
            ]
        },
        {
            "activityTitle": "**Streak: 0** surveys in a row",
            "activitySubtitle": "Survey expires in 15 days on 4/6/2017"
        }
    ]
}</script>
</head>
<body>
This is a sample body
</body>
</html>
"""

def main(argv):
    """The entry point for the script"""
    sender = ""
    password = ""

    try:
        opts, _args = getopt.getopt(argv, 'u:p:', ['user=', 'password='])
    except getopt.GetoptError:
        print('sendactionablemessage.py -u <username> -p <password>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-u':
            sender = arg
        elif opt == '-p':
            password = arg

    if (not sender) or (not password):
        print('sendactionablemessage.py -u <username> -p <password>')
        sys.exit(2)

    print('Sending mail from', sender)
    send_message(sender, password)

def send_message(sender, password):
    """Sends a message from sender to self
    Keyword arguments:
    sender -- The email address of the user that will send and receive the message
    password -- The password for the user
    """
    msg = MIMEText(HTML_CONTENT, 'html')
    msg['Subject'] = 'Test message'
    msg['From'] = sender

    conn = SMTP(SMTP_SERVER, SMTP_PORT)
    try:
        conn.starttls()
        conn.set_debuglevel(False)
        conn.login(sender, password)
        conn.sendmail(sender, sender, msg.as_string())
    finally:
        conn.quit()

    print('Sent the mail')

if __name__ == '__main__':
    main(sys.argv[1:])