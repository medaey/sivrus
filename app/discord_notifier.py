import requests

def send_discord_notification(
    webhook_url,
    content=None,
    username="Sivrus",
    embed_title=None,
    embed_description=None
):
    data = {
        "username": username
    }

    # message texte
    if content:
        data["content"] = content

    # embed optionnel
    if embed_title or embed_description:
        data["embeds"] = [{
            "title": embed_title or "",
            "description": embed_description or ""
        }]

    try:
        response = requests.post(
            webhook_url,
            json=data,
            timeout=10  # ✅ important
        )

        response.raise_for_status()

        print(f"[DISCORD] Sent ({response.status_code})", flush=True)
        return True

    except requests.exceptions.RequestException as e:
        print(f"[DISCORD ERROR] {e}", flush=True)
        return False