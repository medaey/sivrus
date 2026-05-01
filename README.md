# Sivrus

Simple personal automation system.

Sivrus is currently a lightweight automation script that sends Discord notifications based on tasks stored in my personal note system ([fnote](https://github.com/medaey/fnote)).

---

## 🚀 Current Features

- Reads tasks from `.fnote/dump.jsonl`
- Detects tasks older than a configurable number of days
- Sends reminders via Discord webhook
- Cron-friendly execution

---

## 🧠 Goal (Vision)

The long-term goal of Sivrus is to evolve into a personal automation assistant that helps reduce daily mental load by connecting multiple tools (notes, emails, finance, etc.).

---

## ▶ Run

```bash
docker compose up -d
````

---

## ⚙️ Config

Create a `.env` file:

```env id="env1"
DISCORD_WEBHOOK=https://discord.com/api/webhooks/XXXX/XXXX
DISCORD_USERNAME=Sivrus

TASK_FILE=/home/user/.fnote/dump.jsonl
TASK_LIMIT_DAYS=14
```