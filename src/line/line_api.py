from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os


def send_message(msg, group_key):
  message = msg
  if(len(msg)>5000):
    message = msg[0:4999]


  line_bot_api = LineBotApi(os.getenv('CHANNEL_KEY'))
  try:
      line_bot_api.push_message(group_key, TextSendMessage(text=message))
      #line_bot_api.push_message(os.getenv('GROUP_ID_TEST'), TextSendMessage(text=message))
  except LineBotApiError as e:
      print(e)