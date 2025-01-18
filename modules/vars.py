import os

API_ID    = os.environ.get("API_ID", "22100695")
API_HASH  = os.environ.get("API_HASH", "0e8f93300ccbbcd56066e6d790b0d3b2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7549444164:AAGM9dctrWprGDzRUsmSc9-LCpRDweclRrA") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
