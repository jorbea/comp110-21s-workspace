"""A vaccination calculator."""

__author__ = 730151647

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta

#python -m exercises.ex01.vaccine_calc
population: int = int(input("Population:"))
doses_administered: int = int(input("Doses administered:"))
doses_per_day: int = int(input("Doses per day:"))

target_percent_integer_vaccinated: float = float(input("Target percent vaccinated:"))  
target_percent_decimal_vaccinated: float = float(target_percent_integer_vaccinated / 100)

day_count: float = round(float(((((target_percent_decimal_vaccinated) * population) - (doses_administered / 2)) / doses_per_day) * 2))

today: datetime = datetime.today()
vaccination_time: timedelta = timedelta(day_count)
future: datetime = today + vaccination_time

print("We will reach " + str(round(target_percent_integer_vaccinated)) + "% vaccination in " + str(day_count) + " days, which falls on " + str(future.strftime("%B %d, %Y") + "."))
