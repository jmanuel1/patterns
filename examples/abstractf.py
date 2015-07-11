"""Abstract factory example."""


import abc
import argparse
from patterns.abstractf import AbstractFactory


class Greeting(metaclass=abc.ABCMeta):

    """Abstract greeting class."""

    def __init__(self):
        """Make a Greeting object."""
        pass

    @abc.abstractmethod
    def greet(self):
        """Print greeting to sys.stdout (abstract method)."""
        pass


class EnglishGreeting(Greeting):

    """English greeting class."""

    def greet(self):
        """Print English greeting to sys.stdout."""
        print('Hello!')


class MandarinGreeting(Greeting):

    """Mandarin greeting class."""

    def greet(self):
        """Print Mandarin greeting to sys.stdout."""
        print('Ni hao!')


def chooser():
    """Abstract factory chooser."""
    if lang == 'english':
        return EnglishGreeting
    elif lang == 'mandarin':
        return MandarinGreeting


arg_parser = argparse.ArgumentParser(description='give a greeting')
arg_parser.add_argument('language', choices=['english', 'mandarin'],
                        help='language to give greeting in')
lang = arg_parser.parse_args().language
greeting_factory = AbstractFactory(chooser)

greeting_factory().greet()
