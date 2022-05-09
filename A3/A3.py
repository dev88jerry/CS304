"""
Merge sort program for a doubly linked list
"""

# A node of the doubly linked list
class Node:
    __slots__ = 'element', 'prev', 'next'

    # Constructor to create a new node
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # Add item to new linked list
    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        elem = node.element
        node.prev = node.next = node.element = None
        return elem

    # Function to merge two linked list
    def merge(self, first, second):
        # check if either list is empty
        if first is None:
            return second

        if second is None:
            return first

        # select the smaller value of each list
        if first.element < second.element:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    # function to do merge sort
    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead

        second = self.split(tempHead)

        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)

        return self.merge(tempHead, second)

    # function to split list
    def split(self, tempHead):
        half1 = half2 = tempHead
        while (True):
            if half1.next is None:
                break
            if half1.next.next is None:
                break
            half1 = half1.next.next
            half2 = half2.next

        temp = half2.next
        half2.next = None
        return temp

    # function to print sorted list, used for debugging
    def printList(self, node):
        temp = node
        print ("List is")
        while(node is not None):
            print (node.element,end=" ")
            temp = node
            node = node.next

"""
Code for merge sort using array
Provided by instructor
"""

def mergeArray(A,p,q,r):  
    n1 = q - p + 1
    n2 = r - q
   # print("\nmerging, p="+str(p)+' q='+str(q)+" r="+str(r)+" n1="+str(n1)+" n2="+str(n2) + ", arr[p:r]="+str(arr[p:r+1]))
    L = []
    R = []
    for i in range(n1):
        L.append(A[p+i])
    for i in range(n2):
        R.append(A[q+i+1])
    L.append(99999)
    R.append(99999)  
   # print('L = ' + str(L) + " R = " + str(R))
    
    i=0
    j=0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            #print("L = ",L)
        else:
            A[k] = R[j]
            j += 1
            #print("R = ",R)
    #print("MERGED = " + str(A)+"\n")
    
def mergesortArray(A,p,r):
   # if p<r:
       # print('p<r? True. p = ' + str(p) +" r = " + str(r))
   # else:
       # print('p<r? False. p = ' + str(p) +" r = " + str(r) +", RETURNING...")
    if p < r:
        q = (p + r) // 2
       # print("calling merge_sort (left half) with p=" + str(p) + ' r='+str(q))
        mergesortArray(A,p,q)
       # print("calling merge_sort(right half) with p="+str(q+1)+' r='+str(r))
        mergesortArray(A,q+1,r)
        mergeArray(A,p,q,r)


"""
main code used to run merge sort with plots
"""
import time
import numpy as np


dll = DoublyLinkedList()
times = []
times2 = []

for i in range(10, 210, 10):
    
    start_t = time.time()
    mergesortArray(np.arange(0,i),0,i-1)
    times2.append(time.time() - start_t)
    
    start_t = time.time()
    for j in range(0, i):        
        dll.push(j)
        dll.head = dll.mergeSort(dll.head)
    

    times.append(time.time() - start_t)
        
    
import matplotlib.pyplot as plt

plt.plot(times, label='merge sort double link list')
plt.plot(times2, label='merge sort array')
plt.legend()
