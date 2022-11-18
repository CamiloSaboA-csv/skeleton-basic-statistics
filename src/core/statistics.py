from typing import Iterable

from core.data_record import Number, Collection
from core.utils import validate_int, MAX_VALUE

class Statistics:
    """
    A class used to represent data statistics
    """

    def __init__(self, count: int) -> None:
        """
        Initializes the stats.
        """
        self._data: Collection = Collection()
        self._count: int = count

    def __repr__(self) -> str:
        """
        Returns the stats as a string.
        """
        return f"Statistics(stats={[repr(self._data)]}, count={self._count})"

    def __setitem__(self, key: int, item: Number) -> None:
        """
        Sets the recorded number for the given key.
        """
        self._data[key] = item

    def __getitem__(self, key: int) -> Number:
        """
        Returns the recorded number for the given key.
        """
        return self._data[key]

    @property
    def count(self) -> int:
        """
        Returns the number of numbers registered in an object of the Statistics class
        """
        return self._count

    @property
    def data(self) -> Collection:
        """
        Returns the stats.
        """
        return self._data

    def keys(self) -> Iterable[int]:
        """
        Returns a list of all the keys in the stats.
        """
        return self._data.keys()

    def less(self, number: int) -> int:
        """
        Returns the number of numbers less than the given number.
        """
        number=validate_int(number)
        return self._data[number].less

    def greater(self, number: int) -> int:
        """
        Returns the number of numbers greater than the given number.
        """
        number=validate_int(number)
        return self._data[number].greater

    def between(self, a: int, b: int) -> int:
        """
        Returns the number of numbers between the two given numbers.
        """
        a=validate_int(a)
        b=validate_int(b)
        if a < b:
            less_than, greater_than = a, b
        else:
            less_than, greater_than = b, a

        return self._count - self._data[less_than].less - self._data[greater_than].greater


class DataCapture:
    def __init__(self):
        """
        Initializes the recorded data.
        """
        self.count: int = 0
        self.data: Collection = Collection()

    def add(self, number: int) -> None:
        """
        Adds the number to the recorded data.
        """
        self.data[validate_int(number)].count += 1
        self.count += 1

    def build_stats(self) -> Statistics:
        """
        Builds the stats from the recorded data.
        """
        stats: Statistics = Statistics(self.count)
        less: int = 0
        greater: int = self.count

        for i in range(1, MAX_VALUE+1):
            stats[self.data[i].value].count = self.data[i].count
            stats[self.data[i].value].less = less
            stats[self.data[i].value].greater = greater - self.data[i].count
            less += self.data[i].count
            greater -= self.data[i].count
            
        return stats
