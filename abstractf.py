"""This module gives a way to make abstract factories."""


class AbstractFactory:

    """Abstract factory class."""

    def __init__(self, chooser):
        """
        Make an AbstractFactory object.

        `chooser` is a function to choose which class to create an instance of.
        """
        self._chooser = chooser

    def __call__(self, *args, **kwargs):
        """
        Create a new object from this abstract factory.

        `*args` and `**kwargs` are passed to the chooser function to choose a
        class, then they are passed to the chosen class.
        """
        return self._chooser(*args, **kwargs)(*args, **kwargs)
