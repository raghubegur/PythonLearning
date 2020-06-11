from datetime import datetime
# myDictionary = {}
# myDictionary['first'] = 'Raghu'
# myDictionary['second'] = 'Channappa'

# print(myDictionary)

# myList = []
# myList.append(myDictionary)
# print(myList)

# myList.append({
#     'first': 'Kaveri',
#     'second': 'Channappa'
# })

# print(myList)
#myDictionary.append()

#myArray
dataFeedId = '10050'
timeStmpNow = str(datetime.now())
myList = {'HDR|',dataFeedId, timeStmpNow}
# myList.append({'HDR',dataFeedId, timeStmpNow})
print(myList)