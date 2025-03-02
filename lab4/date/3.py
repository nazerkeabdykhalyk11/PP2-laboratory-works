import datetime

def drop_microseconds():
    now = datetime.datetime.now().replace(microsecond=0)
    return now

print(f"\nCurrent datetime without microseconds: {drop_microseconds()}")
