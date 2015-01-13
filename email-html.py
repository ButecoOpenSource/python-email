import smtplib
from email.mime.text import MIMEText

de = 'seumail@gmail.com'
para = ['outroemail@gmail.com']

msg = MIMEText('Exemplo de email HTML do &lt;b&gt;Buteco Open Source&lt;b/&gt;.', 'html', 'utf-8')
msg['From'] = de
msg['To'] = ', '.join(para)
msg['Subject'] = 'Buteco Open Source'

raw = msg.as_string()

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('seumail@gmail.com', 'suasenha')
smtp.sendmail(de, para, raw)
smtp.quit()
