def send_mail(sender,to):
  server = SMTP('smtp.gmail.com',587)
  server.ehlo()
  server.starttls()
  server.ehlo()
  server.login('daamjano@gmail.com','Qwerty123%')
  subject = 'Test Mail'
  body = '''Hurray we succeeded, this is a test mail to make sure that you recieve it in good health :)
            This is an automated mail!! check check :*)'''

  msg = f'subject: {subject} \n\n {body}'

  server.sendmail(sender,to,msg)
  print('mail sent!!! hurray parwwwrriiiii')
  server.quit()