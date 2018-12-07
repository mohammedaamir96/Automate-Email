import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me="mohammedaamir020@gmail.com"
you="mohammedaamir96@gmail.com"

msg=MIMEMultipart('alternative')
msg['subject']= "Promo"
msg['from']= me
msg['to']= you
html='''\
<!Doctype>
<html>
<head>
<body>
<style>
table, th, td {
   border: 1px solid black;
}
</style>
<table style="width:50%">
 <tr>
    <th>filename</th>
    <th>type</th>
    <th>size</th>
    <th>Date & Time</th>
  </tr>
  <tr>
    <td> </th>
    <td> </th>
    <td> </th>
    <td> </th>
  </tr>
   <tr>
    <td> </th>
    <td> </th>
    <td> </th>
    <td> </th>
  </tr>
  <tr>
    <td> </th>
    <td> </th>
    <td> </th>
    <td> </th>
  </tr>
  <tr>
    <td> </th>
    <td> </th>
    <td> </th>
    <td> </th>
  </tr>
  <tr>
    <td> </th>
    <td> </th>
    <td> </th>
    <td> </th>
  </tr>
  <tr>
    <td> </th>
    <td> </th>
    <td> </th>
    <td> </th>
  </tr>
  </body>
  </head>
  </html>
'''
part1=MIMEText(html, 'html')
msg.attach(part1)
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('mohammedaamir020@gmail.com', 'aamir1996')
mail.sendmail(me,you,msg.as_string())
print("msg sent sucessfully")