from datetime import datetime, timedelta

"""
case_day = day used for testing purposes
target_day = the variable that pycleball eventually intends to run.
    It is one week from whatever today's date is because this is the signup horizon in Bedford.
"""

#CASE_DAY
case_day = datetime(2025, 9, 4, 18, 45)
case_day_end   = case_day + timedelta(minutes=30)
case_day_start_time = case_day.strftime("%I:%M %p")  # Output: hh:mm PM
case_day_end_time = case_day_end.strftime("%I:%M %p")  # Output: hh:mm PM
case_day_my_session_string = f"{case_day.strftime("%a, %b %-d @ %-I:%M")}-{case_day_end.strftime("%-I:%M%p")}" # Output: Ddd, Mmm d @ h:mm-h:mmAM
case_day_hmmAP = case_day.strftime("%-I:%M%p")[:-1]  # Output: u:mmPM
case_day_for_registering = "4.0-5.0 " + case_day_hmmAP

def day_next_sign_up_opp_24_hours():
    tomorrow = datetime.now() + timedelta(days=1)
    minutes = datetime.now().minute
    next_interval = (minutes // 15 + 1) * 15
    if next_interval == 60:
        return tomorrow.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        return tomorrow.replace(minute=next_interval, second=0, microsecond=0)


#TARGET_DAY
one_week_from_today = datetime.now() + timedelta(weeks=1)
target_day = one_week_from_today.replace(hour=18, minute=0, second=0, microsecond=0)
target_day_url_string = target_day.strftime("%Y-%m-%d")  # Output: 2025-06-08

def get_date_one_week_before_today(datetime_input):
    date_one_week_before_date_input = datetime_input - timedelta(weeks=1)
    return date_one_week_before_date_input.strftime("%Y-%m-%d")

def get_url_for_session_starting_on(datetime_input):
    url_base = "https://playtimescheduler.com/index.php?go=next&startDate="
    full_url = url_base + get_date_one_week_before_today(datetime_input)
    return full_url


if __name__ == "__main__":
    print(f"'My Session' Date Format String--------------------------------{case_day_my_session_string}")
    print(f"Mobley's Session click time------------------------------------{case_day_hmmAP}")
    print(f"Mobley's registration string to click on ----------------------{case_day_for_registering}")
    print(f"Formatted date one week before {case_day}-------------{get_date_one_week_before_today(case_day)}")
    print(f"Tomorrow's next earliest sign up opportunity--------------------{day_next_sign_up_opp_24_hours()}")
