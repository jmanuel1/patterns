"""This module gives a way to make abstract factories"""

class AbstractFactory:

    """Abstract factory class"""

    def __init__(self, chooser):
        self._chooser = chooser

    def __call__(self, *args, **kwargs):
        return self._chooser(*args, **kwargs)(*args, **kwargs)
