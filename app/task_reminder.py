import os
import json
from datetime import datetime, timedelta


def get_old_tasks():
    task_file_path = os.getenv("TASK_FILE")

    if not task_file_path:
        raise ValueError("TASK_FILE manquant")

    task_limit_days = int(os.getenv("TASK_LIMIT_DAYS", 14))
    limit_date = datetime.now() - timedelta(days=task_limit_days)

    tasks = []

    with open(task_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                task = json.loads(line)

                task_date = datetime.strptime(
                    task["date"],
                    "%Y-%m-%d %H:%M"
                )

                if task_date < limit_date:
                    tasks.append(task)

            except:
                continue

    return tasks