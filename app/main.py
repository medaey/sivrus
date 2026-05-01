import os, time
from dotenv import load_dotenv
from discord_notifier import send_discord_notification as send_notification
from task_reminder import get_old_tasks

load_dotenv()

webhook = os.getenv("DISCORD_WEBHOOK")
username = os.getenv("DISCORD_USERNAME", "Notifier")

interval = int(os.getenv("NOTIFICATION_INTERVAL_SECONDS", 3600))

if not webhook:
    raise ValueError("DISCORD_WEBHOOK manquant")

while True:
    print(f"Next check in {interval}s", flush=True)
    time.sleep(interval)

    tasks = get_old_tasks()

    if tasks:
        msg = "\n".join(f"@here ⏰ {t['note']}" for t in tasks)
        send_notification(webhook, msg, username)
        print("Notification sent", flush=True)