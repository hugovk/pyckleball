from datetime import datetime
# case_day = datetime(2025, 10, 4, 13, 45)
from date_variables import case_day_my_session_string, case_day_for_registering, get_url_for_session_starting_on, case_day_hmmAP, get_date_one_week_before_today, day_next_sign_up_opp_24_hours

from case_create import case_create
from case_common import initialize_case
from case_register import case_register
from case_delete import case_delete

if __name__ == "__main__":
    user_type = "registrant"
    print(f"case_day_my_session_string--------------------{case_day_my_session_string}")
    print(f"case_day_hmmAP--------------------------------{case_day_hmmAP}")
    print(f"case_day_for_registering----------------------{case_day_for_registering}")
    print(f"get_date_one_week_before_today(case_day)------{get_date_one_week_before_today(case_day)}")
    print(f"get_url_for_session_starting_on(case_day)-----{get_url_for_session_starting_on(case_day)}")
    print(f"day_next_sign_up_opp_24_hours-----------------{day_next_sign_up_opp_24_hours()}")

    # case_create()
