# Helper functions — password hashing, code generation, email sending
# These are tools that your endpoints call, not endpoints themselves

import bcrypt        # hashes passwords so we never store plain text
import random        # generates random numbers for verification codes
import smtplib       # connects to Gmail's email server to send emails
from email.mime.text import MIMEText  # formats the email message
import os
from dotenv import load_dotenv

load_dotenv()


# ---- PASSWORD HELPERS ----

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


# ---- CODE GENERATION ----

def generate_code() -> str:
    return str(random.randint(100000, 999999))


# ---- EMAIL SENDING ----

def send_email(to_email: str, code: str):
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")

    msg = MIMEText(f"Your verification code is: {code}")
    msg["Subject"] = "Your Verification Code"
    msg["From"] = smtp_email
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_email, smtp_password)
        server.send_message(msg)
