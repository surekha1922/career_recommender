import smtplib
from config import get_secret

def send_otp(email, otp):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(
        get_secret("EMAIL_USER"),
        get_secret("EMAIL_PASS")
    )

    msg = f"Subject: OTP Login\n\nYour OTP is: {otp}"

    server.sendmail(get_secret("EMAIL_USER"), email, msg)
    server.quit()