try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import time, requests, urllib2, webbrowser, os, csv
import geocoder,math
from pandas import DataFrame

#&markers=color:blue%7Clabel:S%7C40.702147,-74.015794

df = DataFrame.from_csv('analysed.csv',sep=',',parse_dates=False)
df.insert(11,'ZIP','NA')
map_string_list = []
safe_markers = []
unsafe_markers = []
lat_long_list = []
safe_zips = []
unsafe_zips = []
final_string = ''

for index,row in df.iterrows():
	lat = row[8]
	lng = row[9]
	source = row[0]
	label = row[7]

	if lat=='NA' and lng == 'NA':
		continue
	
	if lat!='NA' and lng != 'NA' and label == 'Safe':
		#map_string = "&markers=color:green%7Clabel:S%"+str(lat)+","+str(lng)
		if not math.isnan(lat) and not math.isnan(lng):
			map_string = "&markers=color:red%7Clabel:U%"+str(lat)+","+str(lng)
			#print "Entered"
			if not 'nan' in map_string:
				#print map_string
				zip_ = geocoder.google([lat,lng],method = 'reverse').postal
				safe_zips.append([source,lat,lng,zip_,"Safe"])
				lat_long_list.append([lat,lng])
				safe_markers.append([source,lat,lng])
				df.set_value(index,'ZIP',zip_)
				#map_string_list.append(map_string)

	elif lat!='NA' and lng != 'NA' and label == 'Unsafe':
		if not math.isnan(lat) and not math.isnan(lng):
			map_string = "&markers=color:red%7Clabel:U%"+str(lat)+","+str(lng)
			#print "Entered"
			if not 'nan' in map_string:
				#print map_string
				#map_string_list.append(map_string)
				zip_ = geocoder.google([lat,lng],method = 'reverse').postal
				unsafe_zips.append([source,lat,lng,zip_,"Unsafe"])
				lat_long_list.append([lat,lng])
				unsafe_markers.append([source,lat,lng])
				df.set_value(index,'ZIP',zip_)

df.to_csv('analysed_with_zips.csv')

'''
	# String generated for static maps
	if lat=='NA' and lng == 'NA':
		continue
	
	if lat!='NA' and lng != 'NA' and label == 'Safe':
		map_string = "&markers=color:green%7Clabel:S%"+str(lat)+","+str(lng)
		if not math.isnan(lat) and not math.isnan(lng):
			map_string = "&markers=color:red%7Clabel:U%"+str(lat)+","+str(lng)
			#print "Entered"
			if not 'nan' in map_string:
				print map_string
				map_string_list.append(map_string)

	elif lat!='NA' and lng != 'NA' and label == 'Unsafe':
		if not math.isnan(lat) and not math.isnan(lng):
			map_string = "&markers=color:red%7Clabel:U%"+str(lat)+","+str(lng)
			#print "Entered"
			if not 'nan' in map_string:
				print map_string
				map_string_list.append(map_string)
	

for item in map_string_list:
	final_string = final_string+item


print "\n\n"+final_string
'''

#print safe_markers
print "*********************************************"
#print unsafe_markers

print len(safe_markers)
print len(unsafe_markers)

for item in safe_zips:
	print item

for item in unsafe_zips:
	print item

'''
open('zipcode_data.csv','wb') 


df = DataFrame.from_csv('zipcode_data.csv',sep=',',parse_dates=False)
df.insert(0,'Source','NA')
df.insert(1,'lat','NA')
df.insert(2,'lng','NA')
df.insert(3,'ZIP','NA')

for index,row in df.iterrows():
	for item in safe_zips:
		src = safe_zips[0]
		lat = safe_zips[1]
		lng = safe_zips[2]
		zip_ = safe_zips[3]
		df.set_value(index,'Source',src)
		df.set_value(index,'lat',lat)
		df.set_value(index,'lng',lng)
		df.set_value(index,'ZIP',zip_)
	for item in unsafe_zips:
		src = unsafe_zips[0]
		lat = unsafe_zips[1]
		lng = unsafe_zips[2]
		zip_ = unsafe_zips[3]
		df.set_value(index,'Source',src)
		df.set_value(index,'lat',lat)
		df.set_value(index,'lng',lng)
		df.set_value(index,'ZIP',zip_)	

df.to_csv('zipcode.csv')
'''

