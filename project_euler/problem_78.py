import math
import numpy as np

class PentagonalNumbers(object):
    def __init__(self):
        self.pointer = 0
    def next(self):
        p = self.pointer / 2 + 1
        if self.pointer % 2 == 1:
            p = -p
        self.pointer += 1
        return p * (3*p - 1) / 2

class Partitions(object):
    def __init__(self):
        self.n = 1
        self.partitions = [1]
        self.pentagonals = PentagonalNumbers()
        self.penta_list = []
        self.penta_list.append(self.pentagonals.next())
    def next(self):
        if len(self.partitions) > self.penta_list[-1]:
            # need to add another penta
            self.penta_list.append(self.pentagonals.next())
        #print self.penta_list[-1], len(self.partitions)
        assert self.penta_list[-1] >= len(self.partitions)
        new_partition = 0
        for i, penta in enumerate(self.penta_list):
            if self.n - penta < 0:
                break
            if (i / 2) % 2 == 1:
                sign = -1
            else:
                sign = 1
            new_partition += sign * self.partitions[self.n - penta]
        self.n += 1
        self.partitions.append(new_partition)
        return new_partition

#P = PentagonalNumbers()
P = Partitions()
#for i in range(30):
#    print P.next()
i = 0
p = P.next()
while(p % 1000000 != 0):
    if i % 100 == 0:
        print i, p
    p = P.next()
    i += 1
print P.n -1
print p
"""
55374
3632530092543578593083233157739676164671583617363389322707108646070926860805348954
17314045435376684389911706807452721591544937406153858232021581676352762505545553421
15855424598920159035413044811245082197335097953570911884252410730174907784762924663654000000
"""