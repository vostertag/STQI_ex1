# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:09:20 2017

@author: victor
"""

from Input import Input

class Sorter:
    
    def __init__(self, toSort = None):
        input = Input(toSort)
        self.toSort = list(input.getArray())
        self.sorted = list(input.getArray())
        self.newPositions = []
        for i in range(len(self.toSort)):
            self.newPositions.append(i)
        
    def heapSort(self):
      # convert aList to heap
      length = len( self.sorted ) - 1
      leastParent = length / 2
      for i in range ( int(leastParent), -1, -1 ):
        self.moveDown( i, length )
     
      # flatten heap into sorted array
      for i in range ( length, 0, -1 ):
        if self.sorted[0] > self.sorted[i]:
          self.swap( self.sorted, 0, i )
          self.moveDown( 0, i - 1 )    
     
    def moveDown(self, first, last ):
      largest = 2 * first + 1
      while largest <= last:
        # right child exists and is larger than left child
        if ( largest < last ) and ( self.sorted[largest] < self.sorted[largest + 1] ):
          largest += 1
     
        # right child is larger than parent
        if self.sorted[largest] > self.sorted[first]:
          self.swap( self.sorted, largest, first )
          # move down to largest child
          first = largest;
          largest = 2 * first + 1
        else:
          return # force exit
     
     
    def swap(self, A, x, y ):
      tmp = A[x]
      temp2 = self.newPositions[x]
      self.newPositions[x] = self.newPositions[y]
      self.newPositions[y] = temp2
      A[x] = A[y]
      A[y] = tmp
      
    def insertionSort(self):
        for i in range(len(self.sorted)):
            for j in range(i, len(self.sorted)):
                if self.sorted[j] < self.sorted[i]:
                    self.swap(self.sorted, i, j)
                    
    def sort(self):
        if len(self.sorted) > 30:
            self.heapSort()
        else:
            self.insertionSort()
      
    def getSorted(self):
        return self.sorted
    
    def getToSort(self):
        return self.toSort
    
    def getNewPositions(self):
        return self.newPositions
    
    
    