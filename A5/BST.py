
class _BSTNode:

    __slots__ = 'key', 'value', 'left', 'right'
    
    def __init__(self, key, value):        
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTMap:

    def __init__(self):        
        self._root = None
        self._size = 0

    def __len__(self):        
        return self._size

    def __getitem__(self, key):
        node = self._findNode(self._root, key)
        if node is None:
            raise KeyError()
        return node.value

    def _findNode(self, subtree, key):
        if subtree is None:
            return None
        elif subtree.key == key:
            return subtree
        elif subtree.key < key:
            return self._findNode(subtree.right, key)
        else:
            return self._findNode(subtree.left, key)

    def __setitem__(self, key, value):
        if self._root is None:
            self._root = _BSTNode(key, value)
            self._size += 1
        else:
            self._setItem(self._root, key, value)

    def _setItem(self, subtree, key, value):

        assert subtree is not None

        # The key has been found:
        if subtree.key == key:
            subtree.value = value

        # The key belongs on the left:
        elif key < subtree.key:
            if subtree.left is None:
                subtree.left = _BSTNode(key, value)
                self._size += 1
            else:
                self._setItem(subtree.left, key, value)

        # The key belongs on the right:
        else:
            if subtree.right is None:
                subtree.right = _BSTNode(key, value)
                self._size += 1
            else:
                self._setItem(subtree.right, key, value)
        
    def __delitem__(self, key):
        val = self.pop(key)
        return val

    def pop(self, key):
        value = self[key]
        self._root = self._bstRemove(self._root, key)
        self._size -= 1
        return value

    def _bstRemove(self, subtree, key):
        # Recursively remove the node containing key from this subtree.
        assert subtree is not None, "Cannot remove non-existent key."

        # Key is in the left subtree:
        if key < subtree.key:
            subtree.left = self._bstRemove(subtree.left, key)
            return subtree

        # Key is in the right subtree:
        elif key > subtree.key:
            subtree.right = self._bstRemove(subtree.right, key)
            return subtree

        # The key has been located at the current node:
        else:
            # This is a leaf
            if subtree.left is None and subtree.right is None:
                return None

            # Only a left child:
            elif subtree.left is not None and subtree.right is None:
                return subtree.left

            # Only a right child:
            elif subtree.left is None and subtree.right is not None:
                return subtree.right

            # Two children:
            else:
                successor = self._bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self._bstRemove(subtree.right, successor.key)
                return subtree
