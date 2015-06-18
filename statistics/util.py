__author__ = 'Mike'


class BaseMap:

    def __init__(self, map=None, name=''):
        if map is None:
            map = {}
        self.map = map
        self.name = name

    def map(self):
        return self.map

    def values(self):
        return self.map.keys()

    def set(self, x, y=0):
        self.map[x] = y

    def items(self):
        return self.map.items()

    def increment(self, x, term=1):
        self.map[x] = self.map.get(x, 0) + term

    def multiply(self, x, factor):
        self.map[x] = self.map.get(x, 0) * factor

    def remove(self, x):
        del self.map[x]

    def total(self):
        return sum(self.map.itervalues())

    def max_like(self):
        return max(self.map.itervalues())


class Histogram(BaseMap):

    def frequency(self, x):
        return self.map.get(x, 0)

    def frequencies(self):
        return self.map.values()


class Pmf (BaseMap):

    def probability(self, x, default=0):
        return self.map.get(x, default)

    def probabilities(self):
        return self.map.values()

    def normalise(self, fraction=0):
        total = self.total()
        factor = float(fraction) / total
        for x in self.map:
            self.map[x] *= factor

    def mean(self):
        mu = 0.0
        for x, p in self.map.iteritems():
            mu += p * x
        return mu

    def variance(self, mu=None):
        if mu is None:
            mu = self.Mean()
            variance = 0.0
        for x, p in self.map.iteritems():
            variance += p * (x - mu)**2
        return variance


def histogram_from_list(list, name=''):
    histogram = Histogram(name)
    [histogram.increment(x) for x in list]
    return histogram


def pmf_from_list(list, name=''):
    histogram = histogram_from_list(list, name)
    return pmf_from_histogram(histogram, name)


def pmf_from_histogram(histogram, name=''):
    map = dict(histogram.map())
    pmf = Pmf(map, name)
    pmf.normalise()
    return pmf











