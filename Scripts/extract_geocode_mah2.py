try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import time, requests, urllib2, webbrowser, os, csv
import geocoder,math
from pandas import DataFrame

#&markers=color:blue%7Clabel:S%7C40.702147,-74.015794

df = DataFrame.from_csv('WEST BENGAL_data.csv',sep=',',parse_dates=False)
df.insert(11,'ZIP','NA')
map_string_list = []
safe_markers = []
unsafe_markers = []
lat_long_list = []
safe_zips = []
unsafe_zips = []
final_string = ''
unsafe_info_window_string = []
safe_info_window_string = []
 
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
				ph_val = row[4]
				ec_val = row[5]
				bod_val = row[6]
				do_val = row[3]
				temp_str = "['<div class=\"info_content\">' +'<h2>"+str(row[0])+"</h2><h3>Safe</h3>' + '<p>"+"<b>ph:</b> "+str(ph_val)+" <b>EC:</b> "+str(ec_val)+" <b>BOD:</b> "+str(bod_val)+" <b>DO:</b> "+str(do_val)+"</p>' + '</div>'],"
				#temp_str1 = [temp_str.decode('string_escape')] 
				#temp_str1 = []
				safe_info_window_string.append(temp_str)

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
				ph_val = row[4]
				ec_val = row[5]
				bod_val = row[6]
				do_val = row[3]
				#['<div class="info_content">' +
        #'<h3>Brooklyn Museum</h3>' +
        #'<p>The Brooklyn Museum is an art museum located in the New York City borough of Brooklyn.</p>' + '</div>']
				#temp_str = """'<div class=\"info_content\">\' +\'<h3>Safe</h3>\' + \'<p>"+"ph: "+str(ph_val)+" EC: "+str(ec_val)+" BOD: "+str(bod_val)+" DO: "+str(do_val)+"</p>\' + \'</div>\'"""
				temp_str = "['<div class=\"info_content\">' +'<h2>"+str(row[0])+"</h2><h3>Unsafe</h3>' + '<p>"+"<b>ph:</b> "+str(ph_val)+" <b>EC:</b> "+str(ec_val)+" <b>BOD:</b> "+str(bod_val)+" <b>DO:</b> "+str(do_val)+"</p>' + '</div>'],"
				#temp_str2 = [temp_str.decode('string_escape')]
				unsafe_info_window_string.append(temp_str)

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




print len(safe_markers)
print len(unsafe_markers)

for item in safe_info_window_string:
	print item

print "*********************************************"

for item in unsafe_info_window_string:
	print item


'''

for item in safe_markers:
	print item

print "*********************************************"

for item in unsafe_markers:
	print item

'''

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

