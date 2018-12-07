import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#return redirect(url_for('success',name = user))
me = "mohammedaamir020@gmail.com"
you = "mohammedaamir96@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Amazon Promo"
msg['From'] = me
msg['To'] = you
html='''\
<!doctype>
<html>
<head>
<body>
<h2><a href="www.amazon.in">Click Here</a></h2>
<p>image has a link</p>
html body="<html><body>Amazon Echo:<br><img src="https://www.amazon.in/Amazon-Echo-Smart-speaker-Powered/dp/B0725W7Q38/ref=sr_1_2?s=amazon-devices&ie=UTF8&qid=1543210221&sr=1-2&keywords=echo",alt="for Email">
</body>
</html>"
</body>
</head>
</html>
'''
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('mohammedaamir020@gmail.com', 'aamir1996')
mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")


