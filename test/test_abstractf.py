"""Test patterns.abstractf (abstract factory)."""

import unittest
from patterns.abstractf import AbstractFactory


class AbstractFactoryTest(unittest.TestCase):

    """patterns.abstractf.AbstractFactory test case."""

    def setUp(self):
        """Test set up."""
        self.iterables = [str, bytes, bytearray, list, tuple, dict, set,
                          frozenset]
        iterator = iter(self.iterables)
        chooser = lambda: next(iterator)
        self.iterable_factory = AbstractFactory(chooser)

    def test_abstract_factory(self):
        """Test abstract factory pattern."""
        actuals = []
        while True:
            try:
                actuals.append(type(self.iterable_factory()))
            except StopIteration:
                break

        self.assertEqual(actuals, self.iterables)
