import os, datetime, smtplib, ssl
from email.message import EmailMessage
from config import load_config

def days_since(iso):
    if not iso: return 9999
    dt = datetime.datetime.fromisoformat(iso.replace("Z", ""))
    return (datetime.datetime.utcnow() - dt).days

def send_email(cfg, days):
    contacts = cfg.get("contacts", [])
    if not contacts:
        print("No contacts defined.")
        return

    msg = EmailMessage()
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = ", ".join(contacts)
    msg["Subject"] = "User has been inactive"
    msg.set_content(f"{cfg['message']}\n\nLast seen: {cfg['last_seen_iso']} ({days} days ago)")

    context = ssl.create_default_context()
    with smtplib.SMTP(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls(context=context)
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        server.send_message(msg)
    print("Email sent to:", contacts)

def main():
    cfg = load_config()
    days = days_since(cfg.get("last_seen_iso"))
    if days >= cfg["threshold_days"]:
        send_email(cfg, days)
    else:
        print(f"{days} days since last login — threshold not reached.")

if __name__ == "__main__":
    main()
