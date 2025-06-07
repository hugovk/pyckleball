# write a python script that prints the date one week from today in the format "YYYY-MM-DD"
from datetime import datetime, timedelta

def get_date_one_week_from_today():
    today = datetime.now()
    one_week_later = today + timedelta(weeks=1)
    return one_week_later.strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(get_date_one_week_from_today())
