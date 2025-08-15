from datetime import datetime
from datetime import timedelta

"""
case_day = day used for testing purposes
target_day = the variable that pycleball eventually intends to run.
    It is one week from whatever today's date is because this is the signup horizon in Bedford.
"""

#CASE_DAY
case_day = datetime(2025, 9, 1, 18)
case_day_end   = case_day + timedelta(minutes=30)
# case_day_day_one_digit = case_day.strftime("%-d")  # Output: 8 (without leading zero)
case_day_start_time = case_day.strftime("%I:%M %p")  # Output: 06:00 PM
case_day_end_time = case_day_end.strftime("%I:%M %p")  # Output: 06:30 PM
case_day_mm_dd_yy = case_day.strftime("%m/%d/%Y")
case_day_my_session_string = f"{case_day.strftime("%a, %b %-d @ %-I:%M")}-{case_day_end.strftime("%-I:%M%p")}"
case_day_hmmap = case_day.strftime("%-I:%M%p")[:-1]  # Output: 6:00PM

#TARGET_DAY
one_week_from_today = datetime.now() + timedelta(weeks=1)
target_day = one_week_from_today.replace(hour=18, minute=0, second=0, microsecond=0)
target_day_url_string = target_day.strftime("%Y-%m-%d")  # Output: 2025-06-08


if __name__ == "__main__":
    print(f"'Add Session' date start format-------{case_day_mm_dd_yy}")
    print(f"'My Session' Date Format String-------{case_day_my_session_string}")
    print(f"Mobley's Session click time-----------{case_day_hmmap}")
