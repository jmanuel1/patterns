import abc
import argparse
from patterns.abstractf import AbstractFactory


class Greeting(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def greet(self):
        pass


class EnglishGreeting(Greeting):

    def greet(self):
        print('Hello!')


class MandarinGreeting(Greeting):

    def greet(self):
        print('Ni hao!')


def chooser():
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
