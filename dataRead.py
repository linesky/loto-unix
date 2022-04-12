import dbm
db=dbm.open("my.db","r")
list1=range(1,50)
for n in list1:
	print str(n)+"\t"+db[str(n)]

