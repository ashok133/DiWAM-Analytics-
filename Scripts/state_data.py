try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import time, requests, urllib2, webbrowser, os, csv
import geocoder
from pandas import DataFrame

df_all_states = DataFrame.from_csv('analysed.csv',sep=',',parse_dates=False)

states = ['MAHARASHTRA','ORISSA','HIMACHAL PRADESH','PUNJAB', 'ASSAM', 'KARNATAKA', 'TAMILNADU', 'WEST BENGAL', 'RAJASTHAN', 'GUJARAT',
			'GOA', 'KERALA', 'TRIPURA', 'MEGHALAYA', 'MIZORAM', 'UTTAR PRADESH', 'ANDHRA PRADESH', 'MADHYA PRADESH']

for state in states: 
	df_state = df_all_states.loc[df_all_states['STATE'] == state]
	fname = str(state)+"_data.csv"
	df_state.to_csv(fname)