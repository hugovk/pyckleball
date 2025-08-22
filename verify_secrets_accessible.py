import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

PRO_USER_NAME = os.getenv("PRO_USER_NAME")
PRO_USER_PASSWORD = os.getenv("PRO_USER_PASSWORD")
REGISTRANT_USER_NAME = os.getenv("REGISTRANT_USER_NAME")
REGISTRANT_USER_PASSWORD = os.getenv("REGISTRANT_USER_PASSWORD")

print(f"PRO_USER_NAME is: {PRO_USER_NAME}")
print(f"PRO_USER_PASSWORD is: {PRO_USER_PASSWORD}")
print(f"REGISTRANT_USER_NAME is: {REGISTRANT_USER_NAME}")
print(f"REGISTRANT_USER_PASSWORD is: {REGISTRANT_USER_PASSWORD}")
