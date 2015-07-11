"""patterns.builder (builder pattern) test."""


import unittest
import patterns.builder


class ArgCatcher:

    """Class to catch arguments passed by a builder."""

    def __init__(self, **kwargs):
        """`**kwargs` passed by a builder and kept in `self.kwargs`."""
        self.kwargs = kwargs


class BuilderTest(unittest.TestCase):

    """Builder test case."""

    def test_builder(self):
        """Test patterns.builder.Builder class."""
        builder = patterns.builder.Builder(ArgCatcher)
        builder.set_string('life, the universe, and everything').set_answer(42)
        arg_catcher = builder.set_question('six by nine').build()
        self.assertEqual({'string': 'life, the universe, and everything',
                          'answer': 42,
                          'question': 'six by nine'},
                         arg_catcher.kwargs,
                         'builder does not properly recieve arguments')
