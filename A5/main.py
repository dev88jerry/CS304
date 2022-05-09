
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2

import sys
import random
import time

from BST import BSTMap
from HashTable import ChainHashMap
from HashTable import ProbeHashMap
from SkipList import SkipList

"""
main code used to test the map ADT and plot time complexity
"""

sys.setrecursionlimit(100000)

timeBSTinsert = []
timeChainInsert = []
timeProbeInsert = []
timeSkipInsert = []

timeBSTget = []
timeChainGet = []
timeProbeGet = []
timeSkipGet = []

timeBSTdel = []
timeChainDel = []
timeProbeDel = []
timeSkipDel = []

hashChain = ChainHashMap()
hashProbe = ProbeHashMap()
skipMap = SkipList()
bstMap = BSTMap()

for i in range(10, 2500, 50):

    # insert items into the 4 data structures   
    start_t = time.time()
    for j in range(i):
        bstMap[j] = j * random.randint(2, i)
    timeBSTinsert.append(time.time() - start_t)    

    start_t = time.time()
    for j in range(i):
        skipMap[j] = j * random.randint(2, i)
    timeSkipInsert.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        hashChain[j] = j * random.randint(2, i)
    timeChainInsert.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        hashProbe[j] = j * random.randint(2, i)
    timeProbeInsert.append(time.time() - start_t)

    # get value from 4 data structures     
    start_t = time.time()
    for j in range(i):
        a = bstMap[j]
    timeBSTget.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        b = skipMap[j]
    timeSkipGet.append(time.time() - start_t)
    
    start_t = time.time()
    for j in range(i):
        c = hashChain[j]
    timeChainGet.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        d = hashProbe[j]
    timeProbeGet.append(time.time() - start_t)

    # delete items from 4 data structures    
    start_t = time.time()
    for j in range(i):
        del bstMap[j]
    timeBSTdel.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        del skipMap[j]
    timeSkipDel.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        del hashChain[j]
    timeChainDel.append(time.time() - start_t)

    start_t = time.time()
    for j in range(i):
        del hashProbe[j]
    timeProbeDel.append(time.time() - start_t)


# plot grah of insert item time
plt.figure(dpi=200)
plt.plot(timeBSTinsert, label='BST Map')
plt.plot(timeSkipInsert, label='Skiplist Map')
plt.plot(timeChainInsert, label='Chain Hash Map')
plt.plot(timeProbeInsert, label='Probe Hash Map')
plt.title('Insert item time')
plt.legend()
plt.show()

# plot graph of get item time
plt1.figure(dpi=200)
plt1.plot(timeBSTget, label='BST Map')
plt1.plot(timeSkipGet, label='Skiplist Map')
plt1.plot(timeChainGet, label='Chain Hash Map')
plt1.plot(timeProbeGet, label='Probe Hash Map')
plt1.title('Get item time')
plt1.legend()
plt1.show()

# plot graph of delete item time
plt2.figure(dpi=200)
plt2.plot(timeBSTdel, label='BST Map')
plt2.plot(timeSkipDel, label='Skiplist Map')
plt2.plot(timeChainDel, label='Chain Hash Map')
plt2.plot(timeProbeDel, label='Probe Hash Map')
plt2.title('Delete item time')
plt2.legend()
plt2.show()


