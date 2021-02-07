"""A vaccination calculator."""

__author__ = "730151647"

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

population: int = int(input("Population:"))
doses_administered: int = int(input("Doses administered:"))
doses_per_day: int = int(input("Doses per day:"))
targt_percnt_int_vaccine: int = int(input("Target percent vaccinated:"))

targt_percnt_float_vaccine: float = float(targt_percnt_int_vaccine / 100)
peple_dosed: int = round(doses_administered / 2)
percnt_population: int = round(targt_percnt_float_vaccine * population)

days: float = round(float((((percnt_population - peple_dosed) / doses_per_day) * 2)))

today: datetime = datetime.today()
vaccination_time: timedelta = timedelta(days)
future: datetime = today + vaccination_time

if ((targt_percnt_int_vaccine <= 0) or (targt_percnt_int_vaccine >= 100)):
    print("Please enter a target percent vaccinated value of 0 to 100.")
else:
    print("We will reach " + str(targt_percnt_int_vaccine) + "% vaccination in " + str(days) + " days.")
    print(("This target will fall on " + str(future.strftime("%B %d, %Y")) + "."))