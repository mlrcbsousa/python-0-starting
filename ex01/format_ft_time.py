import time as t
import datetime as dt

current_time = t.time()

# %e is without 0 padding, e.g. 1 instead of 01. %B is the full month name.
epoch_date = dt.datetime.fromtimestamp(0).strftime("%B %e, %Y").replace('  ', ' ')

# %d is with 0 padding. %b is the abbreviated month name.
current_date = dt.datetime.now().strftime("%b %d %Y")

# {current_time:,.4f} - This formats the current_time floating-point number to
#                       have 4 decimal places with commas as thousands separators.
# {current_time:.2e}  - This formats the current_time as a floating-point number
#                       in scientific notation with 2 decimal places.

print(f"Seconds since {epoch_date}: {current_time:,.4f} or {current_time:.2e} in scientific notation")
print(current_date)
