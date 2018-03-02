class Mailsending():

    @staticmethod
    def send_mail(recipient, subject, message):
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText

        username = "logparser@itelligence.hu"
        # password = "sender's password" if it is need

        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        try:
            mailServer = smtplib.SMTP('gitlab.ithint.local', 25)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            # mailServer.login(username, password)
            mailServer.sendmail(username, recipient, msg.as_string())
            mailServer.close()
            print('sent mail to ' + recipient + ' on ' + subject)

        except:
            print('Unable to send email')