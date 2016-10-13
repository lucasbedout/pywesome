import pywesome

def collect(entities):
    return Pywesome(entities)

class Pywesome:

    entities = []

    def __init__(self, entities):
        self.entities = entities 

    def __getattr__(self, name):
        try:
            return object.__getattr__(self, name)
        except AttributeError:
            def forward(*args, **kwargs):
                return getattr(pywesome, name)(self.entities, *args, **kwargs)
            return forward

    def append(self, item):
        self.entities.append(item)

    def pop(self, key):
        return self.entities.pop(key)

    def prepend(self, item):
        self.entities.insert(0, item)

    def count(self):
        return len(self.entities)

    def to_list(self):
        return self.entities

    def to_json(self):
        return self.json()



