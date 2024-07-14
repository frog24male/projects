
import smtplib, ssl

def send_emaill(message):

    host="smtp.gmail.com"
    port=465

    user_name="fa7222518@gmail.com"
    password="crac wuun exsg lmcl"

    receiver='frog24male@gmail.com'
    context=ssl.create_default_context()
    message="""\
    Subject: Hello

    This is a test email.
    """
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(user_name,password)
        server.sendmail(user_name,receiver,message)