import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mailer:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(Mailer.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(from_addr=self.login, to_addrs=msg['To'], msg=msg.as_string())

        ms.quit()

    def receive(self, header=None):
        mail = imaplib.IMAP4_SSL(Mailer.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email.decode("utf-8"))
        mail.logout()


if __name__ == '__main__':
    # login = 'login@gmail.com'
    # password = 'qwerty'
    login = 'kfi.unknown@gmail.com'
    password = 'xpdonxexoclntvhf'
    mailer = Mailer(login=login, password=password)

    subject = 'Subject'
    recipients = ['cut-throat2008@yandex.ru', 'vasya@email.com', 'petya@email.com']
    message = 'Message'
    mailer.send_message(subject=subject, recipients=recipients, message=message)
    header = None
    mailer.receive()
