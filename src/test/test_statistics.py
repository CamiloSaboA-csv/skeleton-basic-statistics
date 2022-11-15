from unittest import TestCase

from core.data_record import Collection, Number
from core.statistics import DataCapture, Statistics
from core.utils import MAX_VALUE


class TestDataRecord(TestCase):
    def test_init(self):
        capture = DataCapture()
        self.assertIsInstance(capture, DataCapture)
        self.assertIsInstance(capture.count, int)
        self.assertIsInstance(capture.data, Collection)
        self.assertEqual(capture.count, 0)
        self.assertEqual(len(capture.data), 0)

    def test_add(self):
        for i in range(1, MAX_VALUE + 1):
            capture = DataCapture()
            capture.add(i)
            self.assertEqual(capture.count, 1)
            self.assertEqual(len(capture.data), 1)
            self.assertEqual(capture.data[i].value, i)

    def test_build_stats(self):
        capture = DataCapture()
        for i in range(1, MAX_VALUE + 1):
            capture.add(i)
        stats = capture.build_stats()
        self.assertIsInstance(stats, Statistics)


def _prepare_stats(numbers):
    capture = DataCapture()
    for number in numbers:
        capture.add(number)

    return capture.build_stats()


class TestStatistics(TestCase):
    def test_init(self):
        stats = Statistics(10)
        self.assertIsInstance(stats, Statistics)
        self.assertIsInstance(stats.count, int)
        self.assertIsInstance(stats.data, Collection)
        self.assertEqual(stats.count, 10)
        self.assertEqual(len(stats.data), 0)

    def test_setitem(self):
        stats = Statistics(10)
        stats[1] = Number(1)
        self.assertEqual(len(stats.data), 1)
        self.assertEqual(stats.data[1].value, 1)

    def test_getitem(self):
        stats = Statistics(10)
        stats[1] = Number(1)
        self.assertEqual(stats[1].value, 1)

    def test_keys(self):
        stats = Statistics(10)
        stats[1] = Number(1)
        stats[2] = Number(2)
        self.assertEqual(list(stats.keys()), [1, 2])

    def test_less(self):
        tests = [
            {
                "numbers": (3, 9, 3, 4, 6),
                "tests_and_results": (
                    (4, 2),
                    (5, 3), 
                    (6, 3),
                    (9, 4),
                ),
            },
        ]

        for test in tests:
            stats = _prepare_stats(test["numbers"])
            with self.subTest(
                    test=test["tests_and_results"][0], result=test["tests_and_results"][1]
            ):
                for number, result in test["tests_and_results"]:
                    self.assertEqual(stats.less(number), result)

    def test_less_error(self):
        tests = [
            {
                "numbers": (3, 9, 3, 4, 6),
                "tests": (-5, 0, 1000, 9999),
            },
        ]

        for test in tests:
            stats = _prepare_stats(test["numbers"])
            for number in test["tests"]:
                with self.subTest(test=number):
                    with self.assertRaises(ValueError):
                        stats.less(number)

    def test_greater(self):
        tests = [
            {
                "numbers": (3, 9, 3, 4, 6),
                "tests_and_results": (
                    (4, 2),
                    (5, 2),
                    (6, 1),
                    (9, 0),
                ),
            },
        ]

        for test in tests:
            stats = _prepare_stats(test["numbers"])
            with self.subTest(
                    test=test["tests_and_results"][0], result=test["tests_and_results"][1]
            ):
                for number, result in test["tests_and_results"]:
                    self.assertEqual(stats.greater(number), result)

    def test_greater_error(self):
        tests = [
            {
                "numbers": (3, 9, 3, 4, 6),
                "tests": (-5, 0, 1000, 9999),
            },
        ]

        for test in tests:
            stats = _prepare_stats(test["numbers"])
            for number in test["tests"]:
                with self.subTest(test=number):
                    with self.assertRaises(ValueError):
                        stats.greater(number)

    def test_between(self):
        tests = [
            {
                "numbers": (3, 9, 3, 4, 6),
                "tests_and_results": (
                    ((3, 6), 4),
                    ((4, 8), 2),
                    ((1, 2), 0),
                    ((5, 2), 3),
                ),
            },
        ]

        for test in tests:
            stats = _prepare_stats(test["numbers"])
            with self.subTest(
                    test=test["tests_and_results"][0], result=test["tests_and_results"][1]
            ):
                for numbers, result in test["tests_and_results"]:
                    self.assertEqual(stats.between(*numbers), result)

    def test_between_error(self):
        tests = [
            {
                "numbers": (3, 9, 3, 4, 6),
                "tests": ((-5, 5), (5, 0), (11, 1000), (1001, 300), (0, 1000)),
            },
        ]

        for test in tests:
            stats = _prepare_stats(test["numbers"])
            for numbers in test["tests"]:
                with self.subTest(test=numbers):
                    with self.assertRaises(ValueError):
                        stats.between(*numbers)
