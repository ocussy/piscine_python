import datetime
import time

date = datetime.datetime.now()
time_now = time.gmtime(0)
time_since = time.time()
scientific_time = "{:.2e}".format(time_since)

print(f"Seconds since January 1, 1970: {time_since:,.4f} or {scientific_time} in scientific notation")
print(date.strftime("%b %d %Y"))