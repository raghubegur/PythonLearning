
def takeSecond(elem):
    return elem[1]


def sorter(item):
    return item['name']

vowelsList = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowelsList.sort()
print('Sorted list:', vowelsList)

vowelsList.sort(reverse=True)
print('Reverse sorted list:', vowelsList)


# list of tuples
listOfTuples = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
listOfTuples.sort(key=takeSecond)

# print sorted listofTuples
print('Sorted list:', listOfTuples)

