import requests

def send_discord_notification(
    webhook_url,
    content=None,
    username="Notifier",
    embed_title=None,
    embed_description=None
):
    data = {
        "username": username
    }

    # Message simple
    if content:
        data["content"] = content

    # Embed optionnel
    if embed_title or embed_description:
        data["embeds"] = [{
            "title": embed_title,
            "description": embed_description
        }]

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        return True, response.status_code
    except requests.exceptions.HTTPError as err:
        return False, str(err)