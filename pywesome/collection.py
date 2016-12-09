from functools import partial

from . import pywesome


class Pywesome(list):

    @staticmethod
    def collect(entities):
        '''
        Re-implement this method if you extend this class. It is used to cast
        list methods that return lists into the intended class.
        '''
        return Pywesome(entities)

    def __getattribute__(self, name, *args, **kwargs):
        '''
        This method override enables the class to include all the methods in the
        pywesome module (file) in the class.
        '''

        if name == '__getstate__':
            # This has to be explicitly raised in this method, not a nested
            # method for pickling (copy) to work properly.
            raise AttributeError()
        try:
            return super().__getattribute__(name, *args, **kwargs)
        except AttributeError as e:
            def forward(*args, **kwargs):
                result = getattr(pywesome, name)(self, *args, **kwargs)
                if isinstance(result, list):
                    return self.collect(result)
                return result
            return forward

    def __getitem__(self, *args, **kwargs):
        result = super().__getitem__(*args, **kwargs)
        try:
            return self.collect(result)
        except TypeError:
            return result

    def __reversed__(self, *args, **kwargs):
        return self.collect(self.__reversed__(*args, **kwargs))

    def __getslice__(self, *args, **kwargs):
        return self.collect(self.__getslice__(self, *args, **kwargs))

    def __add__(self, *args, **kwargs):
        return self.collect(self.__add__(self, *args, **kwargs))

    def __mul__(self, *args, **kwargs):
        return self.collect(self.__mul__(self, *args, **kwargs))

    def count(self):
        return len(self)

    def prepend(self, item):
        self.insert(0, item)

    def to_list(self):
        return list(self)

    def to_json(self):
        return self.json()

