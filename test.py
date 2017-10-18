from Sorter import Sorter
import time
from random import *
import matplotlib.pyplot as plt
import unittest
import sys
 

class TestSorter(unittest.TestCase):
 
    def test_sort_array(self):
        sorter = Sorter([9,6,8,9,1])
        sorter.sort()
        self.assertEqual(sorter.getSorted(), [1,6,8,9,9])
    
    def test_various_arrays(self):
        arraySize = [1,29,30,31,100,1000,10000]
        problem = False;
        for i in arraySize:
            vet = [randint(-1000,1000) for _ in range(i)]
            sorter = Sorter(vet)
            sorter.sort()
            if not checkSorting(sorter.getSorted()):
                problem = True
        self.assertFalse(problem)  
        
    def test_specific_arrays(self):
        problem = False;
        specificArrays = [[0 for _ in range(100)], [randint(-100,-1) for _ in range(100)], [randint(1,100) for _ in range(100)],
                           [0,145,0,0,0,698,15], [0,-145,0,0,0,-698,-15], [0,-145,0,0,10,698,-15]]
        for array in specificArrays:
            hs = Sorter(array)
            hs.heapSort();
            ins = Sorter(array)
            ins.insertionSort()
            if not checkSorting(hs.getSorted()) or not checkSorting(ins.getSorted()):
                problem = True
        self.assertFalse(problem)    
    
    def test_various_inputs(self):
        problem = False;
        inputs = ["array.txt", "1,5,1,60,50,90", [1,8,9,4,5,7,1,2]]
        for i in inputs:
            sorter = Sorter(i)
            sorter.sort()
            if not checkSorting(sorter.getSorted()):
                problem = True
        self.assertFalse(problem)
        
    def test_auxiliary_array(self):
        arraySize = [1,5,29,30,31,100,1000,10000]
        problem = False;
        for i in arraySize:
            vet = [randint(-1000,1000) for _ in range(i)]
            sorter = Sorter(vet)
            sorter.sort()
            if not checkAuxiliary(sorter.getNewPositions(), sorter.getToSort(), sorter.getSorted()):
                print(len(sorter.getNewPositions()))
                problem = True
        self.assertFalse(problem)  
        
    def test_wrong_inputs(self):
        wrongInputs = ["fileName", "5,,,,j899,6,6,6,", None, [1.5555,2.6589,58]]
        for i in wrongInputs:
            self.assertRaises(ValueError, Sorter, i)
    
    def test_performance(self):
        results = []
        results2 = []
        xAxis = []
        start = 1
        end = 1000
        
        for i in range(start, end):
            xAxis.append(i)
            array = []
            for k in range(i):
                array.append(randint(0, 100))
            start = time.clock()
            s = Sorter(array)
            s.sort();
            end = time.clock()
            results.append(end-start);
        
        
        plt.plot(xAxis, results,label='With initialization')
        plt.legend(["Our sorting algorithm"])
        plt.xlabel('Number of elements in array')
        plt.ylabel('Time in seconds')
        plt.show()
        
        

if __name__ == '__main__':
    unittest.main()


def checkSorting(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    
    return True

def checkAuxiliary(positions, notSorted, sortedArray):
    for i in range(len(positions)):
        if sortedArray[i] != notSorted[positions[i]]:
            return False
    return True