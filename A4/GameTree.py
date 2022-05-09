"""
Game tree data type
CS304 Assignment 4

"""
from collections import deque


class GameTree:
    class _Node:
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []
            # list of references to other nodes using queue

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def _validate(self, p):
            if not isinstance(p, self.Position):
                raise TypeError('p is not a position')
            if p._container is not self:
                raise ValueError('p is not this container')
            if p._node._parent is p._node:
                raise ValueError('p not valid')
            return p._node

        def _makePosition(self, node):
            return self.Position(self, node) if node is not None else None

    # ------GameTree items

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def root(self):
        return self._makePosition(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._makePosition(node._parent)

    def child(self, p):
        node = self._validate(p)
        return self._makePosition(node._children)

    def numChildren(self, p):
        node = self._validate(p)
        return len(node._children)

    def addRoot(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._makePosition(self._root)

    def addChild(self, p, e):
        node = self._validate(p)
        tmp = self._Node(e, node)
        node._children.push(tmp)
        self._size += 1
        return self._makePosition(tmp)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._children = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        ret = None
        if node._parent is not None:
            temp = node._parent

            for i in range(len(temp._children)):
                tmpNode = temp._children.index(i)
                if tmpNode._element == node._element:
                    ret = temp._children.pop(i)

        self._size -= 1

        return self._makePosition(ret)

    def breadthFirst(self):
        if not self.isEmpty():
            breadthQueue = deque()
            breadthQueue.appendleft(self._root)
            while len(breadthQueue) != 0:
                p = breadthQueue.popleft()
                #self.printBoard(p._node._element)

                for c in self.child(p):
                    breadthQueue.appendleft(c)

            return breadthQueue

    def depthFirst(self):
        if not self.isEmpty():
            depthQueue = deque()
            depthQueue.appendleft(self._root)
            for p in self._children:
                #yield p
                depthQueue.appendleft(p)
                if len(p._children) is not None:
                    for other in p._children:
                        # yield other
                        depthQueue.appendleft(other)

        return depthQueue

