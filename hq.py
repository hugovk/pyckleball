from datetime import datetime, timedelta
import schedule
import time
from pytz import timezone
import sys

from case_create import case_create
from case_delete import case_delete
from case_register import case_register
from case_deregister import case_deregister
from print_with_color import print_blue
from date_variables import day_next_sign_up_opp_24_hours


# case_day = datetime(2025, 10, 5, 13, 45)
case_day = day_next_sign_up_opp_24_hours()

headless_mode = True
yes_pause = False
sign_up_24_hr_advance = True

def job():
    # case_create(case_day, yes_pause, user_type, headless_mode, sign_up_24_hr_advance)
    # case_delete(case_day, yes_pause, user_type, headless_mode)
    case_register(case_day, yes_pause, "registrant", headless_mode)
    # case_deregister(case_day, yes_pause, "registrant", headless_mode)
    sys.exit("Job completed. Exiting script.")  # Terminate the script

datetime_to_run = datetime.now()
# datetime_to_run = datetime.now() + timedelta(seconds=15)
string_to_run = datetime_to_run.strftime("%H:%M:%S")
print(string_to_run)
schedule.every().day.at(string_to_run, timezone("America/New_York")).do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
