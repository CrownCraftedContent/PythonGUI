import smtplib  # simple mail transfer protocol library

sender = "crowncraftedcontent@gmail.com"
receiver = "thepmilly@gmail.com"
password = "password123"
subject = "Python emailtest"
body = "I wrote an email"

# header
message = f"""From Nickname{sender}
To: TheirNickname{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
