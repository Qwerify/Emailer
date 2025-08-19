from email.message import EmailMessage
import smtplib
verification_codes = {}
async def send_code(email: str,username:str):
    verification_codes[email] = f"Hi, {username}"
    sender_email = "qwerify.ceo@gmail.com"
    sender_password = "ilca hxxo sulk vvgl"
    msg = EmailMessage()
    msg["Subject"] = "Qwerify, make your day"
    msg["From"] = sender_email
    msg["To"] = email
    msg.add_alternative(f"""<!DOCTYPE html><html><head><style>body {{font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;background-color: #f4f4f7;color: #333;padding: 20px;}}.email-container {{max-width: 480px;margin: auto;background-color: #ffffff;border-radius: 10px;padding: 30px;box-shadow: 0 4px 12px rgba(0,0,0,0.1);}}.header {{font-size: 24px;font-weight: bold;color: #4a00e0;text-align: center;margin-bottom: 20px;}}.code {{font-size: 28px;font-weight: bold;text-align: center;background-color: #f1f3ff;padding: 15px;border-radius: 8px;color: #000;letter-spacing: 3px;margin: 20px 0;}}.footer {{margin-top: 30px;font-size: 14px;color: #777;text-align: center;}}</style></head><body><div class="email-container"><div class="header">🔐 Qwerify Verification</div><p><strong>Hello,</strong></p><p>You're just one step away from unlocking the full Qwerify experience.</p><p><strong>Your verification code:</strong></p><div class="code">{verification_codes[email]}</div><p>If you didn't request this code, you can safely ignore this email.</p><div class="footer">— The Qwerify Team 🚀</div></div></body></html>""", subtype='html')
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
    except Exception as e:
        print(e)