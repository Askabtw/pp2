from datetime import datetime, timedelta

#1
fiveDB = datetime.now() - timedelta(days = 5)
#print('5 days before :', fiveDB)



#2
today = datetime.now()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)
#print("yesterday: ", yesterday, "today", today, "tomorrow:", tomorrow )



#3
dt = datetime.now()
dtm = dt.replace(microsecond = 0)
#print(dtm)


#4
dt = datetime.now()
fiveDB = datetime.now() - timedelta(days = 5)
delta = dt - fiveDB
print(delta.total_seconds())