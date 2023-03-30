# Sets of useful searching functions.


# Finds and returns the lowest value in the list.
def findMin(inputList):
    tempMin = inputList[0]
    for i in range(len(inputList)):
        if inputList[i] < tempMin:
            tempMin = inputList[i]
    return tempMin


# Finds and returns the highest value in the list.
def findMax(inputList):
    tempMax = inputList[0]
    for i in range(len(inputList)):
        if inputList[i] > tempMax:
            tempMax = inputList[i]
    return tempMax


# Determines if the list has unique numbers. If it does not then
# it will return the numbers that are the same.
def hasUniqueNumbers(inputList):
    isUnique = True  # Used as a flag to determine if it is unique.
    tempList = []
    duplicateNumbers = []  # Created in case there is duplicate numbers.
    for i in range(len(inputList)):
        if inputList[i] in tempList:
            isUnique = False
            duplicateNumbers.append(inputList[i])
        tempList.append(inputList[i])
    print(duplicateNumbers)
    return isUnique


# Searches a list for a value and returns a boolean value
# if it is found.
def linearSearch(inputList, inputNumber):
    hasNumber = False
    for i in range(len(inputList)):
        if i == inputNumber:
            hasNumber = True
            break
    return hasNumber


# Searches a list for a value but uses binary search operation so
# the time is reduced since it uses a slice of a list.
def binarySearch(inputList, inputNumber):
    numberFound = False
    listStart = 0
    listEnd = len(inputList)
    while listStart < listEnd - 1:
        mid = int((listStart + listEnd) / 2)
        if inputList[mid] == inputNumber:
            numberFound = True
            break
        elif inputList[mid] < inputNumber:
            listStart = mid
        else:
            listEnd = mid
    return numberFound
