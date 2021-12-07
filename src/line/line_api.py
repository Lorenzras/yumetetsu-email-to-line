from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import time

import os

def send_message(msg, group_key):
  line_bot_api = LineBotApi(os.getenv('CHANNEL_KEY'))
  try:
      line_bot_api.push_message(group_key, TextSendMessage(text=msg))
  except LineBotApiError as e:
      print(e)

  print("something")
  time.sleep(5.5)    # Pause 5.5 seconds