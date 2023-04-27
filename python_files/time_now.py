from datetime import datetime

now = datetime.now()

# display time 24 hour
print(now.strftime("%H:%M:%S"))

# display tme 12 hour
print(now.strftime("%I:%M:%S %p"))