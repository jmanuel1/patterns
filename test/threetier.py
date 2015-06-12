import unittest, unittest.mock, patterns.threetier
from patterns.threetier import DataTier, LogicTier, PresentationTier as PresTier


class TestThreeTier(unittest.TestCase):

    def setUp(self):
        self._abstract_methods = {}
        for cls in (DataTier, LogicTier, PresTier):
            self._abstract_methods[cls.__name__] = cls.__abstractmethods__
            cls.__abstractmethods__ = set()
        self.pres_tier = PresTier()

    def test_data_tier(self):
        self.assertEqual(self.pres_tier.logic_tier.data_tier.data_store, None)

    def test_logic_tier(self):
        self.assertEqual(self.pres_tier.logic_tier.process_and_load('key'),
                         None)

    def test_pres_tier(self):
        inputs = iter(('store this that', 'load this', 'invalid'))
        outputs = iter(("datum 'that' stored at 'this'", "data at 'this' is "
                                                    "None", 'invalid cmd '
                                                            'line'))
        patterns.threetier.input = lambda p: self.assertEqual(p, '> ') or \
                                             next(inputs)
        patterns.threetier.print = lambda s: self.assertEqual(s, next(outputs))
        for i in range(3):
            self.pres_tier.interact()

        patterns.threetier.input, patterns.threetier.print = input, print
