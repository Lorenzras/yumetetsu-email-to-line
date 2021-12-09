
import os

def getGroupIdByMailBox(mailBox):
  if (mailBox in ["fujisawa@yumetetsu.jp", "toyohashi@yumetetsu.jp"]):
    return os.getenv('GROUP_ID_FUJISAWA')
  elif (mailBox in ["yawata@yumetetsu.jp", "info@yumetetsu.jp"]):
    return os.getenv('GROUP_ID_TOYOKAWA')
  else:
    return os.getenv('GROUP_ID_TEST')
