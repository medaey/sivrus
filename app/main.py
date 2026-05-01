import os, time, random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from discord_notifier import send_discord_notification as send_notification
from task_reminder import get_old_tasks

load_dotenv()

task_file_path = os.getenv("TASK_FILE")
webhook = os.getenv("DISCORD_WEBHOOK")
username = os.getenv("DISCORD_USERNAME", "Notifier")

while True:
    # aléatoire dans les 2 prochaines minutes
    delay = random.randint(10, 12)

    run = datetime.now() + timedelta(seconds=delay)

    print("Next run in", delay, "seconds")

    time.sleep(delay)

    tasks = get_old_tasks()
    if tasks:
        msg = "\n".join(f"@here ⏰ {t['note']}" for t in tasks)
        send_notification(webhook, msg, username)

    time.sleep(5)