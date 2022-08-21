import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Regarding Your Request'
    body = 'You request has been confirmed'

    msg = f'subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'kipro135@gmail.com', msg)
