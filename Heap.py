import math

class Heap:
    def __init__(self):
        self.heap = []

    def getLeftChildIndex(self,parentIndex):
        return 2 * parentIndex+1
    def getRightChildIndex(self, parentIndex):
        return 2* parentIndex + 2
    def getParentIndex(self, childIndex):
        return math.floor((childIndex-1)/2)
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)< len(self.heap)
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < len(self.heap)
    def hasParent(self, index):
        return self.getParentIndex(index)>=0

    def leftChild(self,index):
        return self.heap[self.getLeftChildIndex(index)][0]
    def rightChild(self,index):
        return self.heap[self.getRightChildIndex(index)][0]
    def parent(self,index):
        return self.heap[self.getParentIndex(index)][0]

    def swap(self,index1,index2):
        temp = self.heap[index1]
        self.heap[index1]= self.heap[index2]
        self.heap[index2] = temp

    def peek(self):
        if(len(self.heap)==0):
            raise Exception('Nothing to look at')

        else:
            return self.heap[0]

    def get(self):
        if(len(self.heap)==0):
            raise Exception('Nothing in heap')
        else:
            temp = self.heap[0]
            self.heap[0]= self.heap[len(self.heap)-1]
            del self.heap[len(self.heap)-1]
            self.heapifyDown()
            return temp

    def add(self,tuple):
        self.heap.append(tuple)
        self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heap)-1
        while(self.hasParent(index) and self.parent(index)>self.heap[index][0]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if(self.hasRightChild(index)and self.rightChild(index)<self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)

            if(self.heap[index]< self.heap[smallerChildIndex]):
                break
            else:
                self.swap(index,smallerChildIndex)

            index = smallerChildIndex
    def empty(self):
        return len(self.heap)==0
    def __str__(self):
        return self.heap.__str__()

class PriorityQueue:
    def __init__(self):
        self.queue = Heap()
    def insertElement(self,tuple):
        self.queue.add(tuple)
    def removeElement(self):
        return self.queue.get()
    def empty(self):
        return self.queue.empty()
    def __str__(self):
        return self.queue.__str__()

