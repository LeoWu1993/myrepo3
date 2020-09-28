import random
from itertools import count
def read_data(filename):
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(',')
            yield map(int, data)

def read_fake_data(filename):
    for i in count():
        sigma = random.random() * 10
        yield (i, random.normalvariate(0, sigma))