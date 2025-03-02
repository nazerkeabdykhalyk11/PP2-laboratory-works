import datetime

def subtract_five_days():
    return datetime.datetime.today() - datetime.timedelta(days=5)

print(f"The date five days ago: {subtract_five_days().date()}")
