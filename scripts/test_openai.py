"""Simple script to verify OpenAI API connectivity via n8n webhook."""
import os
import requests

n8n_webhook = os.getenv("N8N_WEBHOOK")
if not n8n_webhook:
    raise SystemExit("Set N8N_WEBHOOK env variable")

payload = {"prompt": "ping"}
resp = requests.post(n8n_webhook, json=payload, timeout=30)
print(resp.status_code)
print(resp.text)
