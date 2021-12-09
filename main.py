
from dotenv import load_dotenv
from src.line.line_api import send_message
from src.line.utils import getGroupIdByMailBox
import os
import sys

load_dotenv()



def main():
    message = "問題が発生しました。管理者にお知らせください。"
    mailbox = ""
    print(len(sys.argv))

    if(len(sys.argv)>1):
        message = sys.argv[1]
        mailbox = sys.argv[2]

    send_message(message,  getGroupIdByMailBox(mailbox))
    #send_message("konnichiwa",  os.getenv('GROUP_ID_FUJISAWA'))


if __name__ == "__main__":
  main()