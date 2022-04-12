import random
import dbm
db=dbm.open("my.db","c")
list1=range(0,50)
random.SystemRandom(random.random())
for n in list1:
	db[str(n)]=str(random.randrange(1,50))

