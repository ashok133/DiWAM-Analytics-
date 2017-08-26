try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import time, requests, urllib2, webbrowser, os, csv
from pandas import DataFrame
import numpy as np

count = 0
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

urls =[]

# Generating download URLS
for i in range(0,8):
	if i == 0:
		urls.append('https://data.gov.in/catalog/status-water-quality-india-2012?title=&file_short_format=&page=')
	else:
		urls.append('https://data.gov.in/catalog/status-water-quality-india-2012?title=&file_short_format=&page='+str(i))

'''
for link in urls:
	#print link
	#url = requests.get('https://data.gov.in/catalog/status-water-quality-india-2012').text
	url = requests.get(link).text
	soup = BeautifulSoup(url)
	for link in soup.findAll("a"):
		curr_link = link.get("href")
		if curr_link.endswith('download'):
			count += 1
			#print curr_link
			#print "Found a CSV!"
			#temp = curr_link.split('/')[4]
			print curr_link
			#curr_link = curr_link.strip('/download')[0]
			#print "Hold on. I see something. It's ",temp
			#response = requests.get(curr_link, stream=True)
			#response = urllib.urlretrieve(curr_link, "Sheet")
			response = urllib2.urlopen(curr_link)
			data = response.read()
			with open("Sheet"+str(count), "wb") as fp:
				fp.write(data)
			webbrowser.get(chrome_path).open(curr_link)

'''

f_counter = 1
# Combining the CSVs
with open('complete_data.csv','a') as fp:
	for file in os.listdir('Sheets'):
		if file.endswith(".csv"):
			file = os.path.join('Sheets',file)
			#print str(file)
			if f_counter == 1:
				for line in open(file):
					fp.write(line)
				f_counter+=1
			else:
				f = open(file)
				# To skip the header of other CSV files
				f.next()
				for line in f:
					fp.write(line)
				f_counter+=1
				f.close()


#Cleaning the data

df = DataFrame.from_csv('complete_data.csv',sep=',',parse_dates=False)
df.replace('', np.nan, inplace=True)
df.dropna(subset=None, inplace=True)
df.drop_duplicates()

df.to_csv('cleaned_by_pandas.csv')

#removing blank rows

'''
writer = csv.writer(output_)
for row in csv.reader(input_):
	if any(row):
		writer.writerow(row)
input_.close()
output_.close()
'''


# To extract column headers
'''
with open(out_,'rb') as fp:
	csv_f = csv.reader(fp)
	column_headers = next(csv_f)
	ncols = len(next(csv_f))
	fp.seek(0)
	

	for iter_ in range(0,1):
		for index in range(0, ncols):
			print str(row[index])

	#Extracting pH, Temp, EC and turbidity

	for row in csv_f: 
		if row[2] not in states:
			states.append(row[2])

	#print len(states)	
	#for item in states:
		#print item

'''

'''
with open(final_csv,'a') as fp:
	with open(out_,'rb') as fp2:
		writer = csv.writer(fp)
		for row in csv.reader(fp2):
			writer.writerow(row[5])
'''
'''
'''



dcopy = DataFrame.from_csv('cleaned_by_pandas.csv',sep=',',parse_dates=False)
cols = [2,3,5,6,8,9,11,12,14,15,17,18,19,20,21,22,23,24,25]
dcopy.drop(dcopy.columns[cols],axis=1,inplace=True)
dcopy.to_csv('dropped_data.csv')

'''

#new_headers = ['Station Code','Location','State','Temp','pH','EC']
'''

'''

df2 = DataFrame.from_csv('cleaned_data.csv',sep=',',parse_dates=False)
dx = df2.iloc[:,(0,1,4,10,13)]
dx.insert(5,'Safe?','NA')
dx.to_csv('meaningful_data.csv')

'''




'''
check1 = open(out_,'rb')
reader_2 = csv.reader(check1)
for i in range(1):
	print reader_2.next()
'''


'''

meaningful_data = open('meaningful_data.csv','rb')
reader_ = csv.reader(meaningful_data)
#for i in range(1):
#	print reader_.next()

min_ph = 6.5
max_ph = 8.5

# The CSV has data in micromho/cm. 1 micromho/cm = 1000 EC (EC=>microSiemen/cm)
min_ec = 0
max_ec = 3000
min_turb = 0
max_turb = 5

ph_unsafe_count = 0


df = DataFrame.from_csv('meaningful_data.csv',sep=',',parse_dates=False)

row_count = df.shape

for index,row in df.iterrows():
	#row_count += 1
	#print row[0],row[2]
	#Checking the pH levels
	if row[3]<=6.5 or row[3]>=8.5:
		#print row[3],"********"
		df.set_value(index,5,"Unsafe")
		#row[5]="Unsafe"
	else:
		df.set_value(index,5,"Safe")
		#row[5]="Safe"

	#if row[4]<=

	#if row['pH [6.5-8.5] - Mean']<=0.5 or row['pH [6.5-8.5] - Mean']>=18.5:
	#	ph_unsafe_count +=1
		#pass

#for index,row in df.iterrows():
#	print row[5]

df.to_csv('meaningful_data.csv')
print ph_unsafe_count
print row_count[0]
print row_count[0] - ph_unsafe_count

'''
'''
		file_name = "Sheet {}:".format(count)+ str(temp)
		with open (file_name, 'wb') as fp:
			for data in response.iter_content():
				fp.write(data)
		'''
	

		#https://data.gov.in/catalog/status-water-quality-india-2012?title=&file_short_format=&page=1