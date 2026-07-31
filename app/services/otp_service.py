# built in module imports
import requests


# custom module imports
from app.config.setting import setting

class OTPService:
    def __init__(self):
        self.api_key = setting.OTP_API_KEY
        self.base_url = setting.OTP_BASE_URL

    async def send_otp(self, phone: str):
        url = f"{self.base_url}/{self.api_key}/SMS/{phone}/AUTOGEN"
        response = requests.get(url)
        data = response.json()

        if data.get("Status") != "Success":
            raise ValueError(data.get("Details", "Failed to send OTP, invalid phone number"))

        return data["Details"]

    async def verify_otp(self, session_id: str, otp: str):
        url = f"{self.base_url}/{self.api_key}/SMS/VERIFY/{session_id}/{otp}"
        response = requests.get(url)
        data = response.json()
        return data["Status"] == "Success"


otp_service = OTPService()