##

#Load the modules required for the LineBot.

```python
from flask import Flask, request, abort
```

```python
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
```

```python
app = Flask(__name__)
```

## Channel Access Token
```python
line_bot_api = LineBotApi('wwqgHPdvCSdYslvVmA/m9CLnmpIw/KZWI6UyPYyx8R9GryRTVPVV77tfot2oKvdLl/ZERWdk21UNzUXAYvVx1JlKU8nfZYjw/e280Gw8KyjpVzym4/CkhZ/2hnNQ/dNXnL2wLAbaTzbIFn6AbAdjsQdB04t89/1O/w1cDnyilFU=')
```
## Channel Secret
```python
handler = WebhookHandler('661c4caeccec933cb9687d4a917df32f')
```
```python
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
```

#Message delivery section
##Welcome greating 
```python
line_bot_api.push_message('U3aa09e9c07cb88c8b2a790f69dbea42d', TextSendMessage(text='歡迎來到Find My Pet!請輸入"開始"'))
```

## Dealing with the messages
```python
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message =  event.message.text
    if message == "哈囉": #打招呼
       line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=789, sticker_id=10857))
    elif message == "再見": #說再見
       line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=789, sticker_id=10871))
    elif message == "開始": #開始以及功能選單
        message = TextSendMessage(text=('主要功能: 1. 請輸入你所在的城市以查詢最近的動物收容所 EX:台北市 2. 請輸入“領養”來獲得更多資訊'))
        line_bot_api.reply_message(event.reply_token, message)
    elif '台北市' in message:  #輸入城市可得附近得流浪動物收容所
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='臺北市動物之家', address='臺北市', latitude=25.063149585995905, longitude=121.60929481112795))
    elif '新北市' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='新北市政府動物保護防疫處', address='新北市', latitude=25.00416243204753, longitude=121.46037156201673))
    elif '台中市' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='臺中市動物之家南屯園區', address='臺中市', latitude=24.147963134061612, longitude=120.57528232641883))
    elif '台南市' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='臺南市動物之家灣裡站', address='臺南市', latitude=22.936919635099983, longitude=120.1944557129039))
    elif '高雄市' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='高雄市壽山動物保護教育園區', address='高雄市', latitude=22.63716562887085, longitude=120.27868294302546))
    elif '桃園市' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='桃園市動物保護教育園區', address='桃園市', latitude=25.00869946587133, longitude=121.02776236876359))
    elif '宜蘭縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='宜蘭縣流浪動物中途之家', address='宜蘭縣', latitude=24.66734722948268, longitude=121.83122645526362))
    elif '新竹縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='新竹縣公立動物收容所', address='新竹縣', latitude=24.82864328995426, longitude=121.01505416876023))
    elif '苗栗縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='苗栗縣生態保育教育中心', address='苗栗縣', latitude=24.499868218200465, longitude=120.7940121975897))
    elif '彰化縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='彰化縣流浪狗中途之家', address='彰化縣', latitude=23.969424242283026, longitude=120.6197269264156))
    elif '南投縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='南投縣公立動物收容所', address='南投縣', latitude=23.90609246989696, longitude=120.66984445524996))
    elif '嘉義縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='嘉義縣流浪犬中途之家', address='嘉義縣', latitude=23.593276999927433, longitude=120.49980383848104))
    elif '臺東縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='臺東縣動物收容中心', address='臺東縣', latitude=22.721962801874383, longitude=121.10053214457591))
    elif '花蓮縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='花蓮縣狗貓躍動園區', address='花蓮縣', latitude=23.805844864623193, longitude=121.4981204264126))
    elif '澎湖縣' in message:
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='澎湖縣流浪動物收容中心', address='澎湖縣', latitude=23.55242754587402, longitude=119.62716313990182))
    elif "領養" in message:  #Carousel linebot選單可以連接到指定網站
        buttons_template_message = TemplateSendMessage(
        alt_text = "領養",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url ="https://images.unsplash.com/photo-1415369629372-26f2fe60c467?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80",
                    title ="領養",
                    text ="領養服務相關資訊",
                    actions=[
                             URIAction(
                                 label='動物收容所一覽表',
                                 uri='https://asms.coa.gov.tw/Amlapp/App/PetsMap1.aspx'
                             ),
                             URIAction(
                                 label='流浪動物媒合平台',
                                 uri='https://asms.coa.gov.tw/Amlapp/App/AnnounceMent.aspx?PageType=Transfer'
                             )
                         ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        message = TextSendMessage(text=('請輸入 "開始"')) #輸入無法判斷的訊息會跳回請輸入Start
        line_bot_api.reply_message(event.reply_token, message)
```

##Activate
```python
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
