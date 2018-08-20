import csv
import urllib.request as req
import codecs
import sys

url = "https://www.treasury.gov/ofac/downloads/sdn.csv"
ftpstream = req.urlopen(url)
obtained_csv = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))


for line in obtained_csv:
    element_found = [line for element in line if sys.argv[1].lower() in element.lower()]
    if element_found:
        print()
        print(element_found)


    #for element in line:
        # if(sys.argv[1].lower() in element.lower()):
        #     print(line)