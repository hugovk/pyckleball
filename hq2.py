from case_create import case_create
from date_variables import day_next_sign_up_opp_24_hours

case_day = day_next_sign_up_opp_24_hours()
headless = True
sign_up_24_hr_advance = True

case_create(case_day, "pro", headless, sign_up_24_hr_advance)
