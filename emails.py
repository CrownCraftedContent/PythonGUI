import smtplib  # simple mail transfer protocol library

sender = "senderemail@gmail.com"
receiver = "receiveremail@gmail.com"
password = "password123"
subject = "Python Email Test"
body = "Here are the contents of the email"

# header
message = f"""From Nickname{sender}
To: TheirNickname{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)  # 587 = default mail submission port
server.starttls()  # start transport layer security

try:
    server.login(sender, password)  # requires less secure app access on gmail account (temporarily at least)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:  # wrong login combo or haven't enabled less secure app access
    print("unable to sign in")
