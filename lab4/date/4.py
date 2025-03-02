import datetime

def date_difference_in_seconds(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

date1 = datetime.datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime.datetime(2024, 2, 10, 12, 0, 0)
print(f"Difference in seconds: {date_difference_in_seconds(date1, date2)}")
