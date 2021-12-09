
from dotenv import load_dotenv
from src.line.line_api import send_message
from src.line.utils import getGroupIdByMailBox
import sys


#Settings
load_dotenv()

def main():
    message = "メッセージはありませんでした。"
    mailbox = "Nothing"

    if(len(sys.argv)>1):
        message = sys.argv[1]
        mailbox = sys.argv[2]

    #logging.debug(f"Mailbox : {mailbox}" )
    send_message(message,  getGroupIdByMailBox(mailbox))


if __name__ == "__main__":
  main()