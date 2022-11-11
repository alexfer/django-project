import smtplib, ssl

import news.settings


def send(sender, subject, message):
    body = 'Subject: {}\n\n{}'.format(subject, message)

    context = ssl.create_default_context()

    with smtplib.SMTP(news.settings.EMAIL_HOST, news.settings.EMAIL_PORT) as server:
        server.starttls(context=context)
        server.login("alexandershtyher@gmail.com", news.settings.EMAIL_HOST_PASSWORD)
        server.sendmail(sender, news.settings.EMAIL_RECEIVER, body)
        server.quit()
