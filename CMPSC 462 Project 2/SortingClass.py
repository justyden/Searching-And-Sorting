# Sets of useful sorting functions.


# Takes in a list and sort it.
def selectionSort(inputList):
    # This loop keeps track of the front index in the current list.
    for i in range(len(inputList)):
        # Used to set a temporary spot that is the lowest value.
        # The index is also noted.
        tempMin = inputList[i]
        tempSpot = i
        for j in range(len(inputList[i:])):
            # This means an element that is lower was found.
            if inputList[j + i] < tempMin:
                tempMin = inputList[j + i]
                tempSpot = j + i
        # This moves the elements to the correct spot.
        inputList[tempSpot] = inputList[i]
        inputList[i] = tempMin


# This takes a list and sorts it.
def insertionSort(inputList):
    # This iterates through the list.
    for i in range(len(inputList) - 1):
        # Compares each element with the next element.
        if inputList[i + 1] < inputList[i]:
            # An element was found out of place.
            tempSpot = i + 1
            tempNumber = inputList[tempSpot]
            while tempSpot >= 0:
                # Finds the spot the element belongs in.
                if inputList[i + 1] <= inputList[tempSpot]:
                    tempSpot = tempSpot - 1
                else:
                    # The spot was found.
                    break
            del inputList[i + 1]
            inputList.insert((tempSpot + 1), tempNumber)


# This takes a list and sorts it.
def bubbleSort(inputList):
    # This is to declare the sorted part of the list.
    stopPoint = len(inputList) - 1
    for i in range(len(inputList)):
        # This determines if the list is sorted through each iteration.
        isSorted = True
        for j in range(len(inputList[:stopPoint])):
            if inputList[j] > inputList[j + 1]:
                # Determines it is not sorted and swaps elements as needed.
                isSorted = False
                tempNumber = inputList[j]
                inputList[j] = inputList[j + 1]
                inputList[j + 1] = tempNumber
        # This determined the list was sorted.
        if isSorted:
            break
        # Moves the elements checked since the last element is sorted.
        stopPoint = stopPoint - 1


# This takes a list as input and sorts it. Uses
# a helper function to allow it to work correctly.
def mergeSort(inputList):
    # This means the list is sorted since it has only 1 element.
    if len(inputList) == 1:
        return inputList
    else:
        # This creates 2 new lists and returns them to the same function while
        # calling the helper to merge them together.
        mid = int(len(inputList) / 2)
        tempList1 = inputList[:mid]
        tempList2 = inputList[mid:]
        # Returns the sorted list.
        return mergeSortHelper(mergeSort(tempList1), mergeSort(tempList2))


# This is the helper function for merge sort. It takes 2
# lists and returns a sorted combination of them.
def mergeSortHelper(inputList1, inputList2):
    tempList = []
    # This makes sure they are not empty
    # and continues to add elements to the new list.
    while ((inputList1 != []) and (inputList2 != [])):
        if inputList1[0] <= inputList2[0]:
            tempList.append(inputList1[0])
            del inputList1[0]
        else:
            tempList.append(inputList2[0])
            del inputList2[0]
    if inputList1 != []:
        for i in range(len(inputList1)):
            tempList.append(inputList1[i])
        del inputList1
    if inputList2 != []:
        for i in range(len(inputList2)):
            tempList.append(inputList2[i])
        del inputList2
    # This returns the new sorted list.
    return tempList
