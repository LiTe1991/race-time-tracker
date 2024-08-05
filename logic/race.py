"""
A dataclass for the race
"""
from dataclasses import dataclass, field
from datetime import timedelta


@dataclass
class Race:
    """
    Properties and methods for a race of a driver
    """
    measured_round_times: list[timedelta] = field(default_factory=list)
    actual_time: timedelta | None = None
    start_time: timedelta | None = None
    actual_round: int = 0
    rounds_to_drive: int = 1
    min_round_time: int = 5  # Minimal round time before event is allowed, avoid event triggering during start

    def reset_race(self):
        """
        Reset values which changed every race
        """
        self.actual_round = 0
        self.measured_round_times = []
        self.actual_time = None
        self.start_time = None

    def set_time_values(self, start_time: timedelta, actual_time: timedelta):
        """
        Set time values to desire values
        :param start_time: New value for class parameter start_time
        :param actual_time: New value for class parameter actual_time
        """
        self.start_time = start_time
        self.actual_time = actual_time

    def update_actual_time(self, current_time: timedelta):
        """
        Update the actual time, for that we subtract given time and start time.
        :param current_time: Time which is used as first value for subtraction
        """
        self.actual_time = current_time - self.start_time

    def is_race_finished(self) -> bool:
        """
        Check if actual round is equals rounds to drive and return the result
        :return: bool: True or False depend on fact if race is finished
        """
        return self.actual_round == self.rounds_to_drive

    def append_round_to_race(self):
        """
        Append new round to race, increase round counter and measure round time.
        """
        print("Append new round to race " + str(self.actual_time))
        self.actual_round = self.actual_round + 1
        self.measured_round_times.append(self.calculate_time_from_measured_times())

    def calculate_time_from_measured_times(self) -> timedelta:
        """
        Calculate time from measured times or use actual time if measured time is empty
        :return: timedelta: calculated time
        """
        if len(self.measured_round_times) > 0:
            calculated_time = self.actual_time - self.measured_round_times[len(self.measured_round_times) - 1]
        else:
            calculated_time = self.actual_time

        return calculated_time

    def min_round_time_reached(self) -> bool:
        """
        Check if min round time is reached or actual time smaller than min round time.
        :return: bool: True if min time is reached or higher
        """
        return self.calculate_time_from_measured_times().total_seconds() > self.min_round_time
