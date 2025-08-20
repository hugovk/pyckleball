import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

print("Trying to verify secrets are loaded...")
biggest_secret1 = os.getenv("BIGGEST_SECRET")
print(f"SEAN LOADED SECRETS SUCCESSFULLY - and my biggest secret is... '{biggest_secret1}'")
super_repo_secret1 = os.getenv("SUPER_REPO_SECRET")
print(f"SUPER REPO SECRET is: {super_repo_secret1}")
