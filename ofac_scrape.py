import csv
import urllib.request as req
import codecs
import sys


#OFAC
url = "https://www.treasury.gov/ofac/downloads/sdn.csv"
ftpstream = req.urlopen(url)
obtained_csv_ofac= csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))

#SAT
opened_csv=open('sdn.csv', 'r')
obtained_csv_sat = csv.reader(opened_csv)

def scrape(**kwargs):

    found_OFAC=[line for line in obtained_csv_ofac if [line for element in line if kwargs['name'].lower() in element.lower() or kwargs['rfc'].lower() in element.lower() ]]
    found_SAT=[line for line in obtained_csv_sat if [line for element in line if kwargs['name'].lower() in element.lower() or kwargs['rfc'].lower() in element.lower() ]]     
    print("OFAC: ")
    for i in found_OFAC:
        print()
        print(i)
    print("SAT ")
    for i in found_SAT:
        print()
        print(i)

kwargs={}

try:
    kwargs['name']=sys.argv[1]
    kwargs['rfc']=sys.argv[2]
    scrape(**kwargs)
except IndexError:
    kwargs['rfc']='_*_'
    scrape(**kwargs)