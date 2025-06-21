from account.models import *
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User 

def send_otp_to_user(to_email):
    otp = random.randint(111,999)
    user = User.objects.get(email = to_email)

    subject =  "Your OTP Verification Code"

    body = "Your One-Time Password (OTP) for account verification "
    from_email = settings.EMAIL_HOST_USER
    to = [to_email]

    html_content = f"""
<html>
<body style="background-color:#f4f4f4; padding: 40px; font-family: Arial, sans-serif; color: #333;">
    <div style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1);">
        <h2 style="color: #24a0fc;"">Hi {user.username},</h2>
        <p style="font-size:16px;">Your One-Time Password (OTP) for verification is:</p>
        <p style="font-size: 22px;font-weight:bold;color: #24a0fc;text-align:center;margin:20px 0;">{otp}</p>
        <p style="font-size:14px;">This OTP is valid for the next 5 minutes. Please do not share it with anyone.</p>
        <hr style="margin:30px 0;">
        <p style="font-size:14px;">Thank you,<br><strong>Your Website Team</strong></p>
    </div>
</body>
</html>
    """
    email = EmailMultiAlternatives(subject, body, from_email,to)
    email.attach_alternative(html_content, "text/html")
    email.send()

    return otp
    
def sign_up_email(to_email):

    subject = "Welcome to Mysite!"

    body = "Thank You for sign. We glab to have you"

    from_email = settings.EMAIL_HOST_USER

    to = [to_email]
    user = User.objects.get(email = to_email)


    html_content =f"""

<html>

<body style="background-color:#f4f4f4; padding: 40px; font-family: Arial, sans-serif; color: #333;">
    <div
        style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1);">
        <h2 style="color:#4CAF50;">Hi {user.username},</h2>
        <p style="font-size:16px;">Thanks for joining [Your Website Name]!
            We're glad to have you with us.</p>
        <p >Feel free to explore and reach out if you need anything.</p>
        <hr style="margin:30px 0;">
        <p style="font-size:14px;">Best,
            <br><strong>The Your Website name TEeam</strong>
        </p>
    </div>
</body>

</html>

"""
    email = EmailMultiAlternatives( subject, body, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()

def sign_in_email(to_email):
    
    subject = "You’ve signed in successfully"
    body = ""

    from_email = settings.EMAIL_HOST_USER

    to = [to_email]
    user = User.objects.get(email = to_email)


    html_content = f"""
<html>

<body style="background-color:#f4f4f4; padding: 40px; font-family: Arial, sans-serif; color: #333;">
    <div
        style="max-width:600px; margin:auto; background:white; padding:30px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1);">
        <h2 style="color:#4CAF50;">Hi {user.username},</h2>
        <p style="font-size:16px;">You just signed in to [Your Website Name].
If this was you, no action is needed.</p>
        <p >If you didn’t sign in, please secure your account immediately.
</p>
        <hr style="margin:30px 0;">
        <p style="font-size:14px;">Best,
            <br><strong>The Your Website name Team</strong>
        </p>
    </div>
</body>

</html>

"""
    email = EmailMultiAlternatives(subject,body, from_email, to)
    email.attach_alternative(html_content, "text/html")
    email.send()