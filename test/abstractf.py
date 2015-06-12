import unittest
from patterns.abstractf import AbstractFactory


class AbstractFactoryTest(unittest.TestCase):

    def setUp(self):
        self.iterables = [str, bytes, bytearray, list, tuple, dict, set,
                         frozenset]
        iterator = iter(self.iterables)
        chooser = lambda : next(iterator)
        self.iterable_factory = AbstractFactory(chooser)

    def test_abstract_factory(self):
        actuals = []
        while True:
            try:
                actuals.append(type(self.iterable_factory()))
            except StopIteration:
                break

        self.assertEqual(actuals, self.iterables)