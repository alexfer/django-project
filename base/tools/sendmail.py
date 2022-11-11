import news.settings
import smtplib
import ssl


def send(sender, subject, message):
    body = 'Subject: {}\n\n{}'.format(subject, message)
    context = ssl.create_default_context()

    with smtplib.SMTP(news.settings.EMAIL_HOST, news.settings.EMAIL_PORT) as server:
        server.starttls(context=context)
        server.login(news.settings.EMAIL_USERNAME, news.settings.EMAIL_PASSWORD)
        server.sendmail(sender, news.settings.EMAIL_RECEIVER, body)
        server.quit()
