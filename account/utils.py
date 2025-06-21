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
        <p style="font-size:14px;">This OTP is valid for the next 10 minutes. Please do not share it with anyone.</p>
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
    