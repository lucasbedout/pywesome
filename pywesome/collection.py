from . import pywesome


def collect(entities):
    return Pywesome.collect(entities)


class Pywesome(object):
    entities = []

    def __init__(self, entities):
        self.entities = entities

    @staticmethod
    def collect(entities):
        '''
        Re-implement this method if you extend this class. It is used to cast
        list methods that return lists into the intended class.
        '''
        return Pywesome(entities)

    def __getattr__(self, name):
        '''
        This method override enables the class to include all the methods in the
        pywesome module (file) in the class.
        '''
        try:
            return object.__getattr__(self, name)
        except AttributeError:
            def forward(*args, **kwargs):
                result = getattr(pywesome, name)(self.entities, *args, **kwargs)
                if isinstance(result, list):
                    return self.collect(result)
                return result

            return forward

    def __getitem__(self, *args, **kwargs):
        result = self.entities.__getitem__(*args, **kwargs)
        try:
            return self.collect(result)
        except TypeError:
            return result

    def __reversed__(self, *args, **kwargs):
        return self.collect(list(self.entities.__reversed__(*args, **kwargs)))

    def __add__(self, *args, **kwargs):
        return self.collect(self.entities.__add__(*args, **kwargs))

    def __mul__(self, *args, **kwargs):
        return self.collect(self.entities.__mul__(*args, **kwargs))

    def __iter__(self, *args, **kwargs):
        return self.entities.__iter__(*args, **kwargs)

    def __repr__(self):
         return 'Pywesome('+ self.entities.__repr__() + ')'
    
    def __str__(self):
         return 'Pywesome('+ self.entities.__str__() + ')'

    def count(self):
        return len(self.entities)

    def append(self, item):
        self.entities.append(item)

    def prepend(self, item):
        self.entities.insert(0, item)

    def pop(self, key=None):
        if not key:
            key = self.count() - 1
        return self.entities.pop(key)

    def to_list(self):
        return self.entities

    def to_json(self):
        return self.json()

