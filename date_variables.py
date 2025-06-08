from datetime import datetime
from datetime import timedelta

# define a case_day which is Sunday, June 8th, 2025 at 6:00 PM Eastern Time
case_day_start = datetime(2025, 6, 8, 18)  # Example date and time
case_day_end   = case_day_start + timedelta(minutes=30)

# case_day_year = case_day_start.strftime("%Y")  # Output: 2025
# case_day_month = case_day_start.strftime("%m")  # Output: 06
# case_day_day_two_digit = case_day_start.strftime("%d")    # Output: 08
case_day_day_one_digit = case_day_start.strftime("%-d")  # Output: 8 (without leading zero)
case_day_start_time_leading_zero = case_day_start.strftime("%I:%M %p")  # Output: 06:00 PM
case_day_end_time_leading_zero = case_day_end.strftime("%I:%M %p")  # Output: 06:30 PM
# case_day_of_week_three_letters = case_day_start.strftime("%a")  # Output: Sun

def get_add_session_start_date() -> str:
    session_start_date = case_day_start.strftime("%m/%d/%Y")
    return session_start_date

def get_one_week_earlier_url_string(datetime_argument: datetime) -> str:
    today = datetime_argument
    one_week_earlier = today + timedelta(weeks=-1)
    one_week_earlier_url_string = one_week_earlier.strftime("%Y-%m-%d")
    return one_week_earlier_url_string

# MY SESSION STRING
def get_my_session_string() -> str:
    case_day_string_appearing_on_my_sessions_pt1 = case_day_start.strftime("%a, %b %d @ %-I:%M")  # Output: Sun, Jun 08 @ 06:00-06:30PM
    case_day_string_appearing_on_my_sessions_pt2 = case_day_end.strftime("%-I:%M%p")
    my_sessions_string = f"{case_day_string_appearing_on_my_sessions_pt1}-{case_day_string_appearing_on_my_sessions_pt2}"
    return my_sessions_string

if __name__ == "__main__":
    print(f"'Add Session' date start format: {get_add_session_start_date()}")
    print(f"'My Session' Date Format String: {get_my_session_string()}")
    print(f"One week earlier url string    : {get_one_week_earlier_url_string(case_day_start)}")
