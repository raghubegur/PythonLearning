from datetime import datetime, timedelta

timeStmpNow = datetime.now()
print('Currnet timeStamp is: ' + str(timeStmpNow))

dateNow = timeStmpNow.date()
print('Date is: ' + str(dateNow))
print('Day: ' + str(dateNow.day))
print('Month: ' + str(dateNow.month))
print('Year: ' + str(dateNow.year))
print('Hour: ' + str(timeStmpNow.hour))
print('Minute: ' + str(timeStmpNow.minute))
print('Second: ' + str(timeStmpNow.second))

timeNow = timeStmpNow.time()
print('Time is: ' + str(timeNow))

oneDay = timedelta(days=1)
yesterday = timeStmpNow - oneDay
print('Yesterday was: ' + str(yesterday))

birthDay = input('When is your birthday (mm/dd/yyyy): ')
birthDayDate = datetime.strptime(birthDay, '%m/%d/%Y')
print('Birthday is: ' + str(birthDayDate))

oneWeek = timedelta(weeks=1)
lastWeek = dateNow - oneWeek
print('Last week was: ' + str(lastWeek))