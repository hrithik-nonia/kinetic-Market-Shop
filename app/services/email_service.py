import smtplib
from email.mime.text import MIMEText
from app.config.setting import setting

class EmailService:
    async def send_verification_email(self, to_email: str, token: str):
        verify_link = f"{setting.FRONTEND_URL}/verify-email?token={token}"
        body = f"Click this link to verify your account: {verify_link}\nThis link expires in 15 minutes."

        msg = MIMEText(body)
        msg["Subject"] = "Verify your email"
        msg["From"] = setting.SMTP_EMAIL
        msg["To"] = to_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(setting.SMTP_EMAIL, setting.SMTP_APP_PASSWORD)
            server.sendmail(setting.SMTP_EMAIL, to_email, msg.as_string())

email_service = EmailService()