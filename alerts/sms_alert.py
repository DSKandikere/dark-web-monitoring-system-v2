from twilio.rest import Client

# Replace with your Twilio credentials
ACCOUNT_SID = "your_twilio_SID_number"
AUTH_TOKEN = "your_twilio_AUTH_TOCKEN"
TWILIO_NUMBER = "your_twilio_NUMBER"
TARGET_NUMBER = "TARGET_NUMBER"

def send_sms_alert(message):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=TARGET_NUMBER
        )

        print("📱 SMS sent successfully")

    except Exception as e:
        print("❌ SMS failed:", e)
