# A program to test and implement searching and sorting
# algorithms.

import random
import sys
import time
import copy
from SearchClass import *
from SortingClass import *


# This takes a number from the user and creates a list of
# that size with random generated numbers.
def generateNumbers(inputSize):
    tempList = []
    for i in range(1, inputSize + 1):
        tempList.append(random.randint(0, 100000))
    return tempList


# This tests the speed of each sort function.
def testSortSpeed(inputSize):
    tempList = generateNumbers(inputSize)
    testList1 = copy.copy(tempList)
    operationSpeed = time.perf_counter()
    selectionSort(testList1)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The time for selection sort was " + str(operationSpeed) + " s.")

    testList2 = copy.copy(tempList)
    operationSpeed = time.perf_counter()
    insertionSort(testList2)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The time for insertion sort was " + str(operationSpeed) + " s.")

    testList3 = copy.copy(tempList)
    operationSpeed = time.perf_counter()
    bubbleSort(testList3)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The time for bubble sort was " + str(operationSpeed) + " s.")

    testList4 = copy.copy(tempList)
    operationSpeed = time.perf_counter()
    testList4 = mergeSort(testList4)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The time for merge sort was " + str(operationSpeed) + " s.")


# This test the speed for the search functions.
def testSearchSpeed(inputSize):
    tempList = generateNumbers(inputSize)
    print(tempList)
    userInput = int(input("Input a number to search. "))
    operationSpeed = time.perf_counter()
    linearSearch(tempList, userInput)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The linear search operation took " +
          str(operationSpeed) + " s.")
    tempList = mergeSort(tempList)
    operationSpeed = time.perf_counter()
    binarySearch(tempList, userInput)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The binary search operation took " +
          str(operationSpeed) + " s.")
    result = binarySearch(tempList, userInput)
    if result:
        print("The value was found.")
    else:
        print("The value was not found.")


# This test the speed of value functions.
def testValues(inputSize):
    tempList = generateNumbers(inputSize)
    operationSpeed = time.perf_counter()
    maxValue = findMax(tempList)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The highest value was " + str(maxValue) + " and it was found in "
          + str(operationSpeed) + " s.")
    operationSpeed = time.perf_counter()
    minValue = findMin(tempList)
    operationSpeed = time.perf_counter() - operationSpeed
    print("The lowest value was " + str(minValue) + " and it was found in "
          + str(operationSpeed) + " s.")


# This calculates the speed and of finding distinct numbers in the list.
def testUniqueNumbers(inputSize):
    tempList = generateNumbers(inputSize)
    operationSpeed = time.perf_counter()
    hasUnique = hasUniqueNumbers(tempList)
    operationSpeed = time.perf_counter() - operationSpeed
    print("It took " + str(operationSpeed) + " s.")
    if hasUnique:
        print("It does have distinct numbers.")
    else:
        print("It does not have distinct numbers.")


testSortSpeed(50000)
