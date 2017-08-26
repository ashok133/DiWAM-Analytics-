try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import time, requests, urllib2, webbrowser, os, csv
import geocoder
from pandas import DataFrame

min_ph = 6.5
max_ph = 8.5

# The CSV has data in micromho/cm. 1 micromho/cm = 1000 EC (EC=>microSiemen/cm)
min_ec = 0
max_ec = 3000
min_turb = 0
max_turb = 5
unassigned_ll = 0

ph_unsafe_count = 0
do_unsafe_count = 0
bod_unsafe_count = 0
ec_unsafe_count = 0
total_unsafe_count = 0



def unsafe_red():
	return ['background-color: red']

def unsafe_green():
	return ['background-color: green']



df = DataFrame.from_csv('dropped_data.csv',sep=',',parse_dates=False)
#df = df2.head(7000)

row_count = df.shape
df.insert(7,'Safe?','NA')


df.insert(8,'lat','NA')
df.insert(9,'lng','NA')

df.insert(10,'Unsafe Parameters','NA')

start = time.time()

for index,row in df.iterrows():
	#row_count += 1
	#print row[0],row[2]
	#Checking the pH levels

	#print "Checking row"+ str(row);
	
	addr = row[0]
	g = geocoder.google(addr)
	try:
		(lat,lng) = g.latlng
	except ValueError:
		(lat,lng) = ('NA','NA')
		unassigned_ll += 1

	df.set_value(index,'lat',lat)
	df.set_value(index,'lng',lng)

	unsafe_params = []
	flag = 0
	'''
	#Faster
	if row[3]<=6.5 or row[3]>=8.5 or row[4]<30 or row[4]>1500 or row[5]<=6.0 or row[7]>2:
		#print row[3],"********"
		df.set_value(index,'Safe?',"Unsafe")
		df.style.apply(unsafe_red)
		ph_unsafe_count+=1
		#row[5]="Unsafe"
	'''
	if row[4]<=6.5 or row[4]>=8.5:
		#print row[3],"********"
		df.set_value(index,'Safe?',"Unsafe")
		df.style.apply(unsafe_red)
		ph_unsafe_count+=1
		total_unsafe_count +=1
		unsafe_params.append('pH')
		flag = 1
		#row[5]="Unsafe"

	if row[5]<30 or row[5]>1500:
		df.set_value(index,'Safe?',"Unsafe")
		df.style.apply(unsafe_red)
		ec_unsafe_count+=1
		unsafe_params.append('EC')
		total_unsafe_count +=1
		flag = 1

	if row[3]<=6.0:
		df.set_value(index,'Safe?',"Unsafe")
		df.style.apply(unsafe_red)
		do_unsafe_count+=1
		unsafe_params.append('DO')
		total_unsafe_count +=1
		flag = 1

	if row[6]>2:
		df.set_value(index,'Safe?',"Unsafe")
		df.style.apply(unsafe_red)
		bod_unsafe_count+=1
		unsafe_params.append('BOD')
		total_unsafe_count +=1
		flag = 1

	if flag==0:
		df.set_value(index,'Safe?',"Safe")
		df.style.apply(unsafe_green)
		unsafe_params.append('NONE')

	df.set_value(index,'Unsafe Parameters',unsafe_params)

		#row[5]="Safe"

	#if row[4]<=

	#if row['pH [6.5-8.5] - Mean']<=0.5 or row['pH [6.5-8.5] - Mean']>=18.5:
	#	ph_unsafe_count +=1
		#pass
end = time.time()
#for index,row in df.iterrows():
#	print row[5]

df.to_csv('analysed.csv')
print "Total sources",row_count[0]
print "Unsafe labels: ",total_unsafe_count
print "Safe labels: ",row_count[0] - total_unsafe_count
print "Unassigned Lat-Longs ",unassigned_ll
print "Unsafe pH bodies: ", ph_unsafe_count
print "Unsafe EC bodies: ", ec_unsafe_count
print "Unsafe DO bodies: ", do_unsafe_count
print "Unsafe BOD bodies: ", bod_unsafe_count




print "Time taken: ",(end-start)," seconds."
