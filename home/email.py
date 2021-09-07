# Email functions
from modules import *
globals().update(import_modules('home.email', globals()))


def validate_email(email, url):
    JUNJUT_EMAIL = os.environ.get('JUNJUT_EMAIL')
    JUNJUT_PASSWORD = os.environ.get('JUNJUT_PASSWORD')

    link = "https://junjut.herokuapp.com/verified/(url)".replace('(url)', url)
    
    plain_email = "https://junjut.github.io/emails/plain_emails/verify_email.txt"
    html_email = "https://junjut.github.io/emails/html_emails/verify_email.html"
    
    with urlopen(plain_email) as file:
        plain_text = file.read().decode('utf-8').replace('(link)', link)
        
    with urlopen(html_email) as file:
        html_text = file.read().decode('utf-8').replace('(link)', link)

    validation_email = MIMEMultipart('alternative')
    validation_email['Subject'] = 'Junjut - Verify Email'
    validation_email['From'] = JUNJUT_EMAIL
    validation_email['To'] = email
    validation_email.attach(MIMEText(plain_text, 'plain'))
    validation_email.attach(MIMEText(html_text, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(JUNJUT_EMAIL, JUNJUT_PASSWORD)
        server.sendmail(JUNJUT_EMAIL, email, validation_email.as_string())
        server.quit()
        return True
    except:
        return False


def send_reset_pass(email, url):
    JUNJUT_EMAIL = os.environ.get('JUNJUT_EMAIL')
    JUNJUT_PASSWORD = os.environ.get('JUNJUT_PASSWORD')

    link = "https://junjut.herokuapp.com/account/reset-password/(url)".replace('(url)', url)
        
    plain_email = "https://junjut.github.io/emails/plain_emails/reset_password_email.txt"
    html_email = "https://junjut.github.io/emails/html_emails/reset_password_email.html"
    
    with urlopen(plain_email) as file:
        plain_text = file.read().decode('utf-8').replace('(link)', link)
            
    with urlopen(html_email) as file:
        html_text = file.read().decode('utf-8').replace('(link)', link)

    validation_email = MIMEMultipart('alternative')
    validation_email['Subject'] = 'Junjut - Reset Password'
    validation_email['From'] = JUNJUT_EMAIL
    validation_email['To'] = email
    validation_email.attach(MIMEText(plain_text, 'plain'))
    validation_email.attach(MIMEText(html_text, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(JUNJUT_EMAIL, JUNJUT_PASSWORD)
        server.sendmail(JUNJUT_EMAIL, email, validation_email.as_string())
        server.quit()
        return True
    except:
        print('Could not send the reset password email.')
        return False


def send_OTPP_email(email, OTPP):
    JUNJUT_EMAIL = os.environ.get('JUNJUT_EMAIL')
    JUNJUT_PASSWORD = os.environ.get('JUNJUT_PASSWORD')
        
    plain_email = "https://junjut.github.io/emails/plain_emails/OTPP_email.txt"
    html_email = "https://junjut.github.io/emails/html_emails/OTPP_email.html"
    
    with urlopen(plain_email) as file:
        plain_text = file.read().decode('utf-8').replace('(OTPP)', OTPP)
            
    with urlopen(html_email) as file:
        html_text = file.read().decode('utf-8').replace('(OTPP)', OTPP)

    validation_email = MIMEMultipart('alternative')
    validation_email['Subject'] = 'Junjut - OTPP'
    validation_email['From'] = JUNJUT_EMAIL
    validation_email['To'] = email
    validation_email.attach(MIMEText(plain_text, 'plain'))
    validation_email.attach(MIMEText(html_text, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(JUNJUT_EMAIL, JUNJUT_PASSWORD)
        server.sendmail(JUNJUT_EMAIL, email, validation_email.as_string())
        server.quit()
        return True
    except:
        print('Could not send the OTPP email.')
        return False

