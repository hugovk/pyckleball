from datetime import datetime, timedelta
from pytz import timezone
from print_with_color import print_blue

def produce_case_day_strings(case_day: datetime):
    case_day_end_datetime = case_day + timedelta(minutes=30)

    # String on "My Sessions" dashboard
    my_session_string = f"{case_day.strftime('%a, %b %-d @ %-I:%M')}-{case_day_end_datetime.strftime('%-I:%M%p')}"  # Output: Ddd, Mmm d @ h:mm-h:mmAM

    # Formatting the start and end times for "+ Add Session" workflow
    add_session_start_time = case_day.strftime("%I:%M %p")  # Output: hh:mm PM
    add_session_end_time = case_day_end_datetime.strftime("%I:%M %p")  # Output: hh:mm PM

    # Date string for registering in bubble or list mode - e.g. '1:45P'
    hmmAP  = case_day.strftime("%-I:%M%p")[:-1]
    for_registering_bubble_mode = "4.0-5.0 " + hmmAP
    for_registering_list_mode = hmmAP + " : Bedford - John Glenn Middle School – 4.0-5.0"

    return {
        'case_day': case_day,
        'add_session_start_time': add_session_start_time,
        'add_session_end_time': add_session_end_time,
        'my_session_string': my_session_string,
        'for_registering_bubble_mode': for_registering_bubble_mode,
        'for_registering_list_mode': for_registering_list_mode
    }

def day_next_sign_up_opp_24_hours() -> datetime:
    ny_tz = timezone("America/New_York")
    now = datetime.now(ny_tz)  # Use New York timezone
    tomorrow = now + timedelta(days=1)
    minutes = now.minute
    next_interval = (minutes // 15 + 1) * 15
    if next_interval == 60:
        return tomorrow.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    else:
        return tomorrow.replace(minute=next_interval, second=0, microsecond=0)

def sign_up_today_for_session_in_24_hours() -> datetime:
    ny_tz = timezone("America/New_York")
    now = datetime.now(ny_tz)  # Use New York timezone
    minutes = now.minute
    next_interval = (minutes // 15 + 1) * 15
    if next_interval == 60:
        return now.replace(minute=0, second=1, microsecond=0) + timedelta(hours=1)
    else:
        return now.replace(minute=next_interval, second=1, microsecond=0)

# def get_date_one_week_before_today(datetime_input: datetime):
#     date_one_week_before_date_input = datetime_input - timedelta(weeks=1)
#     return date_one_week_before_date_input.strftime("%Y-%m-%d")

def get_url_for_session_on(datetime_input: datetime):
    url_base = "https://playtimescheduler.com/index.php?go=next&startDate="
    date_one_week_before_date_input = datetime_input - timedelta(weeks=1)
    date_one_week_before_input_formatted = date_one_week_before_date_input.strftime("%Y-%m-%d")
    # date_one_week_before_input_formatted = get_date_one_week_before_today(datetime_input)
    full_url = url_base + date_one_week_before_input_formatted
    return full_url

if __name__ == "__main__":
    print_blue("FOR RIGHT NOW")
    case_day = datetime.now()
    case_day_strings = produce_case_day_strings(case_day)
    print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    print("")

    print_blue("FOR A CASE DAY IN THE PAST:")
    case_day = datetime(1015, 10, 4, 13, 45)
    case_day_strings = produce_case_day_strings(case_day)
    print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    print("")

    print_blue("NEXT 24-HR SIGN UP SESSION:")
    case_day = day_next_sign_up_opp_24_hours()
    case_day_strings = produce_case_day_strings(case_day)
    print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
    print("")

    print_blue("MOMENT TO SIGN UP FOR TOMORROW'S 24-HR SIGN UP SESSION:")
    case_day = sign_up_today_for_session_in_24_hours()
    case_day_strings = produce_case_day_strings(case_day)
    print(f"case_day_strings['my_session_string']--------------------{case_day_strings['my_session_string']}")
    print(f"case_day_strings['add_session_start_time']---------------{case_day_strings['add_session_start_time']}")
    print(f"case_day_strings['add_session_end_time']-----------------{case_day_strings['add_session_end_time']}")
    print(f"case_day_strings['for_registering_bubble_mode']----------{case_day_strings['for_registering_bubble_mode']}")
    print(f"case_day_strings['for_registering_list_mode']------------{case_day_strings['for_registering_list_mode']}")
    print(f"get_url_for_session_on(case_day)-------------------------{get_url_for_session_on(case_day)}")
