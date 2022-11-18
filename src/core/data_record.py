from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

from core.utils import validate_int, MAX_VALUE


@dataclass()
class Number:
    def __init__(self, value: int):
        """
        Initializes the recorded number.
        """
        self.value: int = value
        self.less: int = 0
        self.greater: int = 0
        self.count: int = 0

    def __str__(self):
        """
        Returns a string representation of the added Number object.
        """
        return str(
            {
                "value": self.value,
                "less": self.less,
                "greater": self.greater,
                "count": self.count,
            }
        )

    def __repr__(self):
        """
        Returns a string representation of the added Number object.
        """
        return f"Number(value={self.value}, less={self.less}, greater={self.greater}, count={self.count})"



@dataclass()
class Collection:
    def __init__(self) -> None:
        """
        Initializes the collection
        """
        self.collection: dict[int, Number] = {}
        self.current_iteration: int = 0

    def __iter__(self) -> Collection:
        """
        Returns an iterator of the stats.
        """
        return self

    # def __next__(self) -> Number:
    #     """
    #     Returns the next iteration lower than MAX_VALUE.
    #     """
    #     while self.current_iteration < MAX_VALUE:
    #         self.current_iteration += 1
    #         if self.current_iteration not in self.collection:
    #             return Number(self.current_iteration)
    #         else:
    #             return self.collection[self.current_iteration]

    #     self.current_iteration = 0
    #     raise StopIteration

    def __repr__(self) -> str:
        """
        Returns a string representation of the Collection object.
        """
        return repr(self.collection)

    def __setitem__(self, key: int, value: Number) -> None:
        """
        Sets the value of the key to the value
        """
        if key < 1 or key > MAX_VALUE:
            raise ValueError(
                f"the number {key} is out of range, the number must be between the values 1 and {str(MAX_VALUE)}")
        self.collection[key] = value

    def __getitem__(self, key: int) -> Number:
        """
        Returns the Number associated with the key
        """
        if key < 1 or key > MAX_VALUE:
            raise ValueError(
                f"the number {key} is out of range, the number must be between the values 1 and {str(MAX_VALUE)}")
        # if key not in self.collection:
        try:
            return self.collection[key]
        except:
            self.collection[key] = Number(key)
            return self.collection[key]

    def __len__(self) -> int:
        """
        Returns the length of the collection
        """
        return len(self.collection)

    def items(self) -> Iterable[tuple[int, Number]]:
        """
        Returns a list of tuples of the form (key, value)
        """
        return self.collection.items()

    def keys(self) -> Iterable[int]:
        """
        Returns a list of the keys
        """
        return self.collection.keys()
