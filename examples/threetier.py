"""3-tier example."""


import patterns.threetier as tiers


class DataTier(tiers.DataTier):

    """Data tier."""

    def __init__(self, dictionary):
        """Initialize with dictionary."""
        self.dictionary = dictionary

    def store(self, key, data):
        """Store some data."""
        self.dictionary[key] = data

    def retrieve(self, key):
        """Get some data."""
        return self.dictionary[key]


class LogicTier(tiers.LogicTier):

    """Logic Tier."""

    def process_and_load(self, *args, **kwargs):
        """Load."""
        return super().process_and_load(*args, **kwargs)

    def process_and_store(self, *args, **kwargs):
        """Store."""
        return super().process_and_store(*args, **kwargs)


class PresentationTier(tiers.PresentationTier):

    """Presentation tier."""

    def __init__(self):
        """Initialize the tier."""
        self.logic_tier = LogicTier(DataTier({}))

    def interact(self):
        """Interact with user."""
        super().interact()


pres_tier = PresentationTier()
while True:
    pres_tier.interact()
