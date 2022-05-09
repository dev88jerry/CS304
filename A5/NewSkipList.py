
from random import randrange

class HeaderNode:
    def __init__(self):
        self._next = None
        self._down = None

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @next.setter
    def next(self, value):
        self._next = value

    @down.setter
    def down(self, value):
        self._down = value


class DataNode:
    def __init__(self, key, value):
        self._key = key
        self._data = value
        self._next = None
        self._down = None

    @property
    def key(self):
        return self._key

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

    @property
    def down(self):
        return self._down

    @data.setter
    def data(self, value):
        self._data = value

    @next.setter
    def next(self, value):
        self._next = value

    @down.setter
    def down(self, value):
        self._down = value


class SkipList:
    def __init__(self):
        self._head = None


    def search(self, key):
        current = self._head

        while current:
            if current.next is None:
                current = current.down
            else:
                if current.next.key == key:
                    return current.next.data
                else:
                    if key < current.next.key:
                        current = current.down
                    else:
                        current = current.next
        return None


    def flip(self):
        return randrange(2)


    def insert(self, key, value):
        
        tower = []
        
        if self._head is None:

            self._head = HeaderNode()
            temp = DataNode(key, value)
            self._head.next = temp
            top = temp
            
            while self.flip() == 1:
                newhead = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                newhead.next = temp
                newhead.down = self._head
                self._head = newhead
                top = temp
        
        else:
            
            current = self._head
            
            while current:
                if current.next is None:
                    tower.append(current)
                    current = current.down
                else:
                    if current.next.key > key:
                        tower.append(current)
                        current = current.down
                    else:
                        current = current.next

            lowest_level = tower.pop()
            temp = DataNode(key, value)
            temp.next = lowest_level.next
            lowest_level.next = temp
            top = temp

        while self.flip() == 1:
            if len(tower) == 0:
                newhead = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                newhead.next = temp
                newhead.down = self._head
                self._head = newhead
                top = temp
            else:
                next_level = tower.pop()
                temp = DataNode(key, value)
                temp.down = top
                temp.next = next_level.next
                next_level.next = temp
                top = temp


class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        return self.collection.search(key)
    
    def __getitem__(self, key):
        self.get(key)
    
    

