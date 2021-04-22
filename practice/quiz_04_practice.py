from __future__ import annotations
"""Practice for Quiz 04."""
"""Questions 12-13 from the Quiz 04 Practice."""

class Time:
    """Time Class."""
    hours: int = 12
    minutes: int = 0

    def __init__(self, h: int, m: int):
        """Constructor."""
        self.hours = h
        self.minutes = m

    def add_time(self, add_time: Time) -> Time:
        """Returns a new time object with the sum of the two times."""
        new_hours = self.hours + add_time.hours
        new_minutes = self.minutes + add_time.minutes
        
        if new_minutes >= 60:
            new_hours += 1
            new_minutes = new_minutes % 60

        new_hours = new_hours % 12
        
        new_time: Time = Time(new_hours, new_minutes)
        return new_time

    def display_time(self) -> None:
        """Print out the time."""
        f"Time is {self.hours} hours and {self.minutes} minutes."

    def display_minutes(self) -> None:
        """Prints out the total minutes."""
        total_minutes = 0
        total_minutes += (self.hours * 60) + self.minutes
        f"{total_minutes} minutes."


t1: Time = Time(10, 50)
t2: Time = Time(4, 20)
new = t1.add_time(t2)

time = new.display_time
print(time)

minutes = new.display_minutes
print(minutes)

t3: Time = t1.add_time(t2)

