"""The builder pattern."""


class Builder:

    """
    Class that can make a builder out of any type (in fact, any *callable*).

    Usage:
    >>> builder = Builder(open)
    >>> file = builder.set_file('file.txt').set_mode('r+').build()
    >>> file.close()
    """

    def __init__(self, cls):
        """
        Make a Builder object.

        `cls` is the class to make an instance of.
        """
        self._cls = cls
        self._kwargs = {}

    def __getattr__(self, attr):
        """
        Overloaded __getattr__ method.

        If `attr` starts with 'set_', the rest of `attr` is used as one of the
        keyword arguments passed to `cls`. Otherwise, if the attribute doesn't
        exist, AttributeError is raised.
        """
        if attr.startswith('set_'):
            def func(value):
                self._kwargs[attr[4:]] = value
                return self
            return func
        else:
            # If the attribute existed, we wouldn't have been called.
            raise AttributeError

    def build(self):
        """Create an instance of `cls` using arguments given to the builder."""
        return self._cls(**self._kwargs)
