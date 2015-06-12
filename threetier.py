"""This module declares abstract base classes useful for laying out a 3-tier
software architecture"""


import abc


class DataTier(metaclass=abc.ABCMeta):
    """Data tier - controls storage and retrieval of data"""

    @abc.abstractmethod
    def __init__(self, data_store):
        self.data_store = data_store

    @abc.abstractmethod
    def store(self, key, data):
        """Store some data"""
        pass

    @abc.abstractmethod
    def retrieve(self, key):
        """Retrieve some data"""
        pass


class LogicTier(metaclass=abc.ABCMeta):
    """Business logic tier - where the data processing is"""

    def __init__(self, data_tier):
        self.data_tier = data_tier

    @abc.abstractmethod
    def process_and_load(self, key, func=lambda x: x):
        """Process the data at a given key"""
        return func(self.data_tier.retrieve(key))

    @abc.abstractmethod
    def process_and_store(self, key, data, func=lambda x: x):
        """Process the `data` parameter with `func`, and store it at `key`"""
        self.data_tier.store(key, func(data))


class PresentationTier(metaclass=abc.ABCMeta):
    """Presentation tier - the user-facing stuff"""

    @abc.abstractmethod
    def __init__(self):
        self.logic_tier = LogicTier(DataTier(None))

    @abc.abstractmethod
    def interact(self):
        """Interact with the user once"""
        string = input('> ')
        tokens = string.split()
        if tokens[0] == 'load' and len(tokens) == 2:
            print('data at {} is {}'.format(
                repr(tokens[1]),
                repr(self.logic_tier.process_and_load(tokens[1]))))
        elif tokens[0] == 'store' and len(tokens) == 3:
            self.logic_tier.process_and_store(tokens[1], tokens[2])
            print('datum {} stored at {}'.format(repr(tokens[2]),
                                                 repr(tokens[1])))
        else:
            print('invalid cmd line')
