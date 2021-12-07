
from dotenv import load_dotenv
from src.line.line_api import send_message
import os
import sys
import time

load_dotenv()



def main():
    message = "長すぎます。"
    print(len(sys.argv))

    if(len(sys.argv)>1):
        message =sys.argv[1]
        if(len(message)>5000):
            message = message[0:4999]


    send_message(message,  os.getenv('GROUP_ID_TEST'))
    #send_message("konnichiwa",  os.getenv('GROUP_ID_FUJISAWA'))
    time.sleep(100.5)    # Pause 5.5 seconds


if __name__ == "__main__":
  main()