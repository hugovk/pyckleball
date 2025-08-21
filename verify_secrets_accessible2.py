import os
from dotenv import load_dotenv

load_dotenv()

# MY_SUPER_REPO_SECRET = os.getenv("my_super_repo_secret")
# PRO_USER_NAME = os.getenv("pro_user_name")
# PRO_USER_PASSWORD = os.getenv("pro_user_password")
# REGISTRANT_USER_NAME = os.getenv("registrant_user_name")
# REGISTRANT_USER_PASSWORD = os.getenv("registrant_user_password")

PRO_USER_NAME = os.getenv("PRO_USER_NAME")
PRO_USER_PASSWORD = os.getenv("PRO_USER_PASSWORD")
REGISTRANT_USER_NAME = os.getenv("REGISTRANT_USER_NAME")
REGISTRANT_USER_PASSWORD = os.getenv("REGISTRANT_USER_PASSWORD")

print(f"PRO_USER_NAME is: {PRO_USER_NAME}")
print(f"PRO_USER_PASSWORD is: {PRO_USER_PASSWORD}")
print(f"REGISTRANT_USER_NAME is: {REGISTRANT_USER_NAME}")
print(f"REGISTRANT_USER_PASSWORD is: {REGISTRANT_USER_PASSWORD}")
