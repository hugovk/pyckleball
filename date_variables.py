from datetime import datetime, timedelta

"""
case_day = day used for testing purposes
target_day = the variable that pycleball eventually intends to run.
    It is one week from whatever today's date is because this is the signup horizon in Bedford.
"""

#CASE_DAY
def produce_case_day(case_day: datetime):
    case_day_end_datetime = case_day + timedelta(minutes=30)

    # Formatting the start and end times for "+ Add Session" workflow
    add_session_start_time = case_day.strftime("%I:%M %p")  # Output: hh:mm PM
    add_session_end_time = case_day_end_datetime.strftime("%I:%M %p")  # Output: hh:mm PM

    # String on "My Sessions" dashboard
    my_session_string = f"{case_day.strftime('%a, %b %-d @ %-I:%M')}-{case_day.strftime('%-I:%M%p')}"  # Output: Ddd, Mmm d @ h:mm-h:mmAM

    hmmAP  = case_day.strftime("%-I:%M%p")[:-1]
    # hhmmAP = case_day.strftime("%I:%M%p")[:-1]

    for_registering_bubble_mode = "4.0-5.0 " + hmmAP
    for_registering_list_mode = hmmAP + " : Bedford - John Glenn Middle School – 4.0-5.0"
    # for_registering_list_mode = "6:00P : Bedford - John Glenn Middle School – 4.0-5.0"

    return {
        'add_session_start_time': add_session_start_time,
        'add_session_end_time': add_session_end_time,
        'my_session_string': my_session_string,
        'hmmAP': hmmAP,
        'for_registering_bubble_mode': for_registering_bubble_mode,
        'for_registering_list_mode': for_registering_list_mode
    }

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
    case_day = produce_case_day(datetime(2025, 10, 4, 13, 45))
    print(f"case_day['add_session_start_time']---------------{case_day['add_session_start_time']}")
    print(f"case_day['add_session_end_time']-----------------{case_day['add_session_end_time']}")
    print(f"case_day['my_session_string']--------------------{case_day['my_session_string']}")
    print(f"case_day['hmmAP']----- --------------------------{case_day['hmmAP']}")
    print(f"case_day['for_registering_bubble_mode']----------{case_day['for_registering_bubble_mode']}")
    print(f"case_day['for_registering_list_mode']------------{case_day['for_registering_list_mode']}")

    # print(f"get_date_one_week_before_today(case_day)------{get_date_one_week_before_today(case_day)}")
    # print(f"day_next_sign_up_opp_24_hours-----------------{day_next_sign_up_opp_24_hours()}")
