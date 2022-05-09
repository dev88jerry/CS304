
import random

class SkipList:
    
    # internal node class
    class Node:        
        __slots__ = 'key', 'value', 'nexts'
        
        def __init__(self, key, value, level):
            self.key = key
            self.value = value
            self.nexts = [None] * level
    
    def __init__(self):
        # The head node does not store any data
        self.Max_level = 32
        self._First = self.Node(None, None, self.Max_level)  # header node
        self._Level = 0
        self._size = 0
        self._prob = 0.5  # is used to generate the random level when adding nodes

    def __getitem__(self, key):
        self.keyCheck(key)
        node = self._First
        for level in range(self._Level - 1, -1, -1):
            # if key is greater than the key of the node. Look forward
            while node.nexts[level] and node.nexts[level].key < key:
                node = node.nexts[level]
            # equal, find, otherwise look down
            if node.nexts[level] and node.nexts[level].key == key:
                return node.nexts[level].value
        return None

    def __setitem__(self, key, value):
        self.keyCheck(key)
        prev = [None] * self._Level
        node = self._First
        for i in range(self._Level - 1, -1, -1):
            while node.nexts[i] and node.nexts[i].key < key:
                node = node.nexts[i]
            if node.nexts[i] and node.nexts[i].key == key:
                oldValue = node.nexts[i].value
                node.nexts[i].value = value
                return oldValue
            prev[i] = node  # save node current level less than key

        newLevel = self.randomLevel()

        newNode = SkipList.Node(key, value, newLevel)
        for i in range(newLevel):
            if i < self._Level:
                newNode.nexts[i] = prev[i].nexts[i]
                prev[i].nexts[i] = newNode
            else:
                self._First.nexts[i] = newNode
        self._size += 1
        self._Level = max(self._Level, newLevel)
        return None

    def __delitem__(self, key):
        self.keyCheck(key)
        prev = [None] * self._Level
        node = self._First
        flag = False  # flag for node if found
        for i in range(self._Level - 1, -1, -1):
            while node.nexts[i] and node.nexts[i].key < key:
                node = node.nexts[i]
            if node.nexts[i].key == key:
                flag = True
            prev[i] = node
        if not flag:
            return None
        removedNode = node.nexts[0]
        # the nexts must be less than or equal to the length of prev
        for i in range(len(removedNode.nexts)):
            prev[i].nexts[i] = removedNode.nexts[i]

        self._size -= 1
        newLevel = self._Level
        while newLevel > 0 and not self._First.nexts[newLevel - 1]:
            newLevel -= 1
        self._Level = newLevel
        return removedNode.value

    def keyCheck(self, key):
        if key != 0 and not key:
            raise AttributeError('Empty Key')

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def randomLevel(self):  
        # generate a random number of layers
        level = 1
        while random.random() < self._prob and level < self.Max_level:
            level += 1
        return level
