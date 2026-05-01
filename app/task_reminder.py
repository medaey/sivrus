import os, json
from datetime import datetime, timedelta

def is_old(date_str, limit_date):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M") < limit_date

def get_old_tasks():
    task_file_path = os.getenv("TASK_FILE")
    task_limit_days = int(os.getenv("TASK_LIMIT_DAYS", 14))

    if not task_file_path:
        raise ValueError("TASK_FILE non défini")

    limit_date = datetime.now() - timedelta(days=task_limit_days)

    tasks = []

    with open(task_file_path) as f:
        for line in f:
            if line.startswith("#"):
                continue
            try:
                task = json.loads(line)
                if is_old(task["date"], limit_date):
                    tasks.append(task)
            except:
                pass

    return tasks