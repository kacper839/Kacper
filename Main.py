import os, time, re, requests
from datetime import datetime

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
URL = "https://www.olx.pl/motoryzacja/samochody/wojewodztwo/pomorskie/?search%5Bfilter_float_price%3Ato%5D=10000&search%5Border%5D=created_at%3Adesc"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "pl-PL,pl;q=0.9"
}

def send(msg):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}, timeout=10)

def check():
    try:
        r = requests.get(URL, headers=HEADERS, timeout=15)
        send(f"✅ BOT POMORZE TEST {r.status_code} - {datetime.now().strftime('%H:%M:%S')}\n{URL}")
    except Exception as e:
        send(f"Błąd: {e}")

if TOKEN and CHAT_ID:
    send("🚀 START Fliphunter Pomorze")
    while True:
        check()
        time.sleep(300)
