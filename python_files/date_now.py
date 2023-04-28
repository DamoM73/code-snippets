from datetime import date
from datetime import datetime

# display today's date
print(date.today())

# display custom date
now = datetime.now()
print(f"{now.day}/{now.month}/{now.year}")