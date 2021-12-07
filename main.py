
from dotenv import load_dotenv
from src.line.line_api import send_message
import os
import sys

load_dotenv()



def main():
    send_message(sys.argv[1],  os.getenv('GROUP_ID_TEST'))
    #send_message("konnichiwa",  os.getenv('GROUP_ID_FUJISAWA'))



if __name__ == "__main__":
  main()