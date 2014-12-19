import smtplib

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

smtp.login('seuemail@gmail.com', 'suasenha')

de = 'seuemail@gmail.com'
para = ['seuemail@gmail.com']
msg = """From: %s
To: %s
Subject: Buteco Open Source

Email de teste do Buteco Open Source.""" % (de, ', '.join(para))

smtp.sendmail(de, para, msg)

smtp.quit()
