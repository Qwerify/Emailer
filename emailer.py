from email.message import EmailMessage
import smtplib
verification_codes = {}
async def send_code(email: str,username:str):
    verification_codes[email] = f"Hi, {username}" # Your custom message here
    sender_email = "qwerify.ceo@gmail.com" # Your email
    sender_password = "Your api password"
    msg = EmailMessage()
    msg["Subject"] = "Qwerify, make your day" # Title
    msg["From"] = sender_email
    msg["To"] = email
    msg.add_alternative(f"""<!DOCTYPE html><html>Your html here</html>""", subtype='html') # To appear like a page (Html)
    msg.set_content("Hello, this is a plain text email body.") # To send raw text
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
    except Exception as e:
        print(e)
