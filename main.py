import os
from dotenv import load_dotenv
from discord_notifier import send_discord_notification as send_notification
from task_reminder import get_old_tasks

load_dotenv()

discord_webhook = os.getenv("DISCORD_WEBHOOK") or (_ for _ in ()).throw(ValueError("DISCORD_WEBHOOK manquant"))
discord_username = os.getenv("DISCORD_USERNAME", "Notifier")

for task in get_old_tasks():
    send_notification(discord_webhook, f"⏰ {task['note']}", discord_username)

print(len(get_old_tasks()))