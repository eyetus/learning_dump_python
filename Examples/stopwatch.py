# Stopwatch using 'time' package
# Importing 'time' module:
import time

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

# wait for user to stop timer
input("Press 'Enter' to stop timer")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")


# importing only the required functions from 'time' package:
from time import localtime, mktime, strftime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# wait for user to stop timer
input("Press 'Enter' to stop timer")

stop_time = localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")