import patterns.threetier as tiers


class DataTier(tiers.DataTier):

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def store(self, key, data):
        self.dictionary[key] = data

    def retrieve(self, key):
        return self.dictionary[key]


class LogicTier(tiers.LogicTier):

    def process_and_load(self, *args, **kwargs):
        return super().process_and_load(*args, **kwargs)

    def process_and_store(self, *args, **kwargs):
        return super().process_and_store(*args, **kwargs)


class PresentationTier(tiers.PresentationTier):

    def __init__(self):
        self.logic_tier = LogicTier(DataTier({}))

    def interact(self):
        super().interact()


pres_tier = PresentationTier()
while True:
    pres_tier.interact()
