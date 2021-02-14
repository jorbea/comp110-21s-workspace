"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730151647"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population, doses, doses_per_day, target)
    date: str = future_date(days)
    if (days == 0):
        print("Please enter a target percent vaccinated [target] value of 0 to 100.")
    else:
        print("We will reach " + str(target) + "% vaccination in " + str(days) + " days.")
        print("This target will fall on " + str(date) + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculates the number of days until the target percent vaccinated is achieved."""
    if ((target < 0) or (target > 100)):
        return 0
    else:
        targt_percnt: float = float(target / 100)
        people_dosed: int = round(doses / 2)
        population_percent: int = round(targt_percnt * population)
        days: int = round(float((((population_percent - people_dosed) / doses_per_day) * 2)))
        return days


def future_date(days: int) -> str:
    """Determines the date [MM, DD, YYYY] in which the target percent vaccinated is achieved."""
    today: datetime = datetime.today()
    vaccination_time: timedelta = timedelta(days)
    future: datetime = today + vaccination_time
    date: str = str(future.strftime("%B %d, %Y"))
    return date


if __name__ == "__main__":
    main()
