from datetime import datetime

# define a case_day which is Sunday, June 8th, 2025 at 6:00 PM Eastern Time
case_day_start = datetime(2025, 6, 8, 18)  # Example date and time
case_day_end   = datetime(2025, 6, 8, 18, 30)

# print("Year:", case_day_start.strftime("%Y"))          # Output: Year:    2025
# print("Month:", case_day_start.strftime("%m"))         # Output: Month:   06
# print("Day:", case_day_start.strftime("%d"))           # Output: Day:     08
# print("Date:", case_day_start.strftime("%Y-%m-%d"))    # Output: Date:    2025-06-08

case_day_start_day = case_day_start.strftime("%d")

# print("Minute:", case_day_start.strftime("%M"))        # Output: Minute:  00
# print("Second:", case_day_start.strftime("%S"))        # Output: Second:  00
# print("Weekday:", case_day_start.strftime("%a"))       # Output: Weekday: Sun
# print("Time:", case_day_start.strftime("%I:%M %p"))    # Output: Time:    06:00 PM


# print("\n" + "CASE DAY END:")
# print("Time:", case_day_end.strftime("%I:%M %p"))    # Output: Time:    06:30 PM
