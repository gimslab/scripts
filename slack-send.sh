read msg

payload='payload={"username": "webhookbot", "text": "'"${msg}"'", "icon_emoji": ":ghost:"}'
curl -X POST --data-urlencode "$payload" https://hooks.slack.com/services/xxxxx
