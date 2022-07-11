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
    if message == "Hi": #打招呼
       line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=789, sticker_id=10857))
    elif message == "Bye": #說再見
       line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=789, sticker_id=10871))
    elif message == "Start": #開始以及功能選單
        message = TextSendMessage(text=('Main Functions: 1. Enter the city you live in to find the closest animal shelter. EX:台北市 2. Enter "Adopt" to get more information'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台北市' in message:  #輸入城市可得附近得流浪動物收容所
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='臺北市動物之家', address='Taipei', latitude=25.063149585995905, longitude=121.60929481112795))
    #輸入城市可得附近得流浪動物收容所 
    elif '新北市' in message:
        message = TextSendMessage(text=('新北市政府動物保護防疫處'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台中市' in message:
        message = TextSendMessage(text=('臺中市動物之家南屯園區, 臺中市動物之家后里園區'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台南市' in message:
        message = TextSendMessage(text=('臺南市動物之家灣裡站, 臺南市動物之家善化站'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '高雄市' in message:
        message = TextSendMessage(text=('高雄市壽山動物保護教育園區, 高雄市燕巢動物保護關愛園區'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '桃園市' in message:
        message = TextSendMessage(text=('桃園市動物保護教育園區'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '宜蘭縣' in message:
        message = TextSendMessage(text=('宜蘭縣流浪動物中途之家'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '新竹縣' in message:
        message = TextSendMessage(text=('新竹縣公立動物收容所'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '苗栗縣' in message:
        message = TextSendMessage(text=('苗栗縣生態保育教育中心'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '彰化縣' in message:
        message = TextSendMessage(text=('彰化縣流浪狗中途之家'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '南投縣' in message:
        message = TextSendMessage(text=('南投縣公立動物收容所'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '雲林縣' in message:
        message = TextSendMessage(text=('雲林縣流浪動物收容所'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '嘉義縣' in message:
        message = TextSendMessage(text=('嘉義縣流浪犬中途之家'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '屏東縣' in message:
        message = TextSendMessage(text=('屏東縣公立犬貓中途之家	'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '臺東縣' in message:
        message = TextSendMessage(text=('臺東縣動物收容中心'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '花蓮縣' in message:
        message = TextSendMessage(text=('花蓮縣狗貓躍動園區'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '澎湖縣' in message:
        message = TextSendMessage(text=('澎湖縣流浪動物收容中心'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '基隆市' in message:
        message = TextSendMessage(text=('基隆市寵物銀行'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '新竹市' in message:
        message = TextSendMessage(text=('新竹市動物保護教育園區'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '嘉義市' in message:
        message = TextSendMessage(text=('嘉義市動物保護教育園區'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '金門縣' in message:
        message = TextSendMessage(text=('金門縣動物收容中心'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '連江縣' in message:
        message = TextSendMessage(text=('連江縣流浪犬收容中心'))
        line_bot_api.reply_message(event.reply_token, message)
    elif 'Adopt' in message: #傳送收容管理系統網址
        message = TextSendMessage(text=('https://asms.coa.gov.tw/Amlapp/App/PetsMap1.apx'))
        line_bot_api.reply_message(event.reply_token,,message)
    else:
        message = TextSendMessage(text=('Please enter "Start"'))
        line_bot_api.reply_message(event.reply_token, message)







import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
