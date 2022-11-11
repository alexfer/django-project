import news.settings as smtp
import smtplib
import ssl


def send(sender, subject, message):
    body = 'Subject: {}\n\n{}'.format(subject, message)
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp.EMAIL_HOST, smtp.EMAIL_PORT) as server:
        server.starttls(context=context)
        server.login(smtp.EMAIL_USERNAME, smtp.EMAIL_PASSWORD)
        server.sendmail(sender, smtp.EMAIL_RECEIVER, body)
        server.quit()
