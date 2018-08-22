import csv
import urllib.request as req
import codecs
import sys

url = "https://www.treasury.gov/ofac/downloads/sdn.csv"
ftpstream = req.urlopen(url)
obtained_csv = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))

def scrape(**kwargs):
    found=[line for line in obtained_csv if [line for element in line if kwargs['name'].lower() in element.lower() or kwargs['rfc'].lower() in element.lower() ]]   
    for i in found:
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