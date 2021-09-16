from os import getenv
from dotenv import load_dotenv
from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

from weather import get_today_weather, get_tom_weather


# .env ファイルをロードして環境変数へ反映
load_dotenv()

CHANNEL_SECRET = getenv("CHANNEL_SECRET")
CHANNEL_ACCESS_TOKEN = getenv("CHANNEL_ACCESS_TOKEN")

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)

    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 入力された文字列を取得
    text_in = event.message.text

    if "今日" in text_in:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=get_today_weather(text_in))
        )
    elif "明日" in text_in:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=get_tom_weather(text_in))
        )
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text_in))


if __name__ == "__main__":
    app.run(port=8080)
