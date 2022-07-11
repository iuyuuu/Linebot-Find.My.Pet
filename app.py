#載入LineBot所需要的模組
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


# 必須放上自己的Channel Access Token

line_bot_api = LineBotApi('wwqgHPdvCSdYslvVmA/m9CLnmpIw/KZWI6UyPYyx8R9GryRTVPVV77tfot2oKvdLl/ZERWdk21UNzUXAYvVx1JlKU8nfZYjw/e280Gw8KyjpVzym4/CkhZ/2hnNQ/dNXnL2wLAbaTzbIFn6AbAdjsQdB04t89/1O/w1cDnyilFU=')

# 必須放上自己的Channel Secret
handler = WebhookHandler('661c4caeccec933cb9687d4a917df32f')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
#歡迎詞
line_bot_api.push_message('U3aa09e9c07cb88c8b2a790f69dbea42d', TextSendMessage(text='Welcome to Find My Pet ! Please enter "Start"'))


# 處理訊息

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message =  event.message.text
    if message == "Hi":
       line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=789, sticker_id=10857))
    elif message == "Bye":
       line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=789, sticker_id=10871))
    else:
        message = TextSendMessage(text='Main Functions: 1. Enter the city you live in to find the closest animal shelter. EX:台北市 /n 2. Enter the name of the shelter to find the current number of stray dogs,cats. EX:新北市五股區公立動物之家 n/ 3. Enter "Where" to get the map of the shelter')
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)