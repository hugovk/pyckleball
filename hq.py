import schedule
import time
from pytz import timezone
import sys

from case_register import case_register
from print_with_color import print_blue
from date_variables import day_next_sign_up_opp_24_hours, sign_up_today_for_session_in_24_hours

# case_day = datetime(2025, 10, 5, 13, 45)
case_day = day_next_sign_up_opp_24_hours()

headless = True
yes_pause = False
sign_up_24_hr_advance = True

def job():
    case_register(case_day, "registrant", headless)
    sys.exit("Job completed. Exiting script.")  # Terminate the script

datetime_to_run = sign_up_today_for_session_in_24_hours()
# datetime_to_run = datetime.now()
# datetime_to_run = datetime.now() + timedelta(seconds=15)
string_to_run = datetime_to_run.strftime("%H:%M:%S")
datetime_to_run_formatted = datetime_to_run.strftime("%Y-%m-%d %H:%M:%S")
print_blue(f"Scheduling job to run at {datetime_to_run_formatted}.")
schedule.every().day.at(string_to_run, timezone("America/New_York")).do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
