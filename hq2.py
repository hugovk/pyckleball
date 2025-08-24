# from datetime import datetime

from case_create import case_create
from case_delete import case_delete
from date_variables import day_next_sign_up_opp_24_hours

case_day = day_next_sign_up_opp_24_hours()

headless_mode = True
yes_pause = False
sign_up_24_hr_advance = True

# case_create(case_day, yes_pause, "pro", headless_mode, sign_up_24_hr_advance)
case_delete(case_day, yes_pause, "pro", headless_mode)
