import time
import csv
import datetime


start = time.time()


days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
writer = open("total4.csv", "wb") 
w = csv.writer(writer) 
w.writerow(["Year","Day","ArrDelay","DepDelay","Origin","Dest","Carrier"])


year = 1987


while year <= 2008:
	reader = open("{}.csv".format(year), "r")
	r = csv.reader(reader)
	next(reader, None)
	i=0
	for row in r:
		try:
			w.writerow([int(row[0]),days[int(row[3])-1],int(row[14]),int(row[15]),str(row[16]),str(row[17]),str(row[8])])
			i+=1
			if i%90000==0:
				print str(i) + " done in "+ str((time.time()-start)/60) + " mins for year " + str(year)	
		except:
			pass
	year += 1
