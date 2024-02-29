# Time

Time in Python is recorded in seconds. Any given time is recorded as the number of seconds since 1st January 1970 (referred at as the epoch).

We will use two different libraries to deal with time:

- [time](https://docs.python.org/3/library/time.html)
- [datetime](https://docs.python.org/3/library/datetime.html)

Both are part of the standard library that comes packaged with Python.

## Pausing

The `sleep` method pauses the program calculation and waits. The argument passes the wait time in seconds.

```{literalinclude} ./python_files/pause.py
:linenos:
```

For more information check **[this freeCOdeCamp article](https://www.freecodecamp.org/news/python-sleep-time-sleep-in-python/)**.

## Current time

The `now` method returns the current local date and time. We also use the `strftime` method to format the date. There are many **[formatting codes](https://docs.python.org/3/library/datetime.html?highlight=now#strftime-and-strptime-format-codes)**.

```{literalinclude} ./python_files/time_now.py
:linenos:
```

For more information check **[this freeCodeCamp artilce](https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/)**


## Current date

Both `today` will return today's date, while `now` will return today's date and time.

The return objects can be refined by using the dot notation asking for the:

- year
- month
- day
- hour
- minute
- second
- microsecond

```{literalinclude} ./python_files/date_now.py
:linenos:
```

## Calculate elapsed time

Since time is recorded in seconds, can perform calculations between two times.

```{literalinclude} ./python_files/elapsed_time.py
:linenos:
```
