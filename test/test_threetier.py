"""patterns.threetier (3-tier arch) test."""


import unittest
import unittest.mock
import patterns.threetier
from patterns.threetier import DataTier, LogicTier
from patterns.threetier import PresentationTier as PresTier


class TestThreeTier(unittest.TestCase):

    """3-tier test case."""

    def setUp(self):
        """Test set up."""
        self._abstract_methods = {}
        for cls in (DataTier, LogicTier, PresTier):
            self._abstract_methods[cls.__name__] = cls.__abstractmethods__
            cls.__abstractmethods__ = set()
        self.pres_tier = PresTier()

    def test_data_tier(self):
        """Data tier test."""
        self.assertEqual(self.pres_tier.logic_tier.data_tier.data_store, None)

    def test_logic_tier(self):
        """Logic tier test."""
        self.assertEqual(self.pres_tier.logic_tier.process_and_load('key'),
                         None)

    def test_pres_tier(self):
        """Presentation tier test."""
        inputs = iter(('store this that', 'load this', 'invalid'))
        outputs = iter(("datum 'that' stored at 'this'",
                        "data at 'this' is None",
                        'invalid cmd line'))
        patterns.threetier.input = lambda p: self.assertEqual(p, '> ') or \
            next(inputs)
        patterns.threetier.print = lambda s: self.assertEqual(s, next(outputs))
        for i in range(3):
            self.pres_tier.interact()

        patterns.threetier.input, patterns.threetier.print = input, print
