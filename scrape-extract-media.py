# this obviously requires twint and urlextract

import os
import sys
from urlextract import URLExtract

extractor = URLExtract()

search = input("search:  ")

print("scraping...")
os.system(f"twint --media -s {search} > {search}.txt")
print("\n\ndone scraping, now extracting links")

file = open(f"{search}.txt", 'r')
lines = file.readlines()
outputFile = open(f"{search}-links.txt", 'w')
# Strips the newline character
for line in lines:
    for link in extractor.gen_urls(line):
        #print(url)
        outputFile.write(f"{link}\n")


print("extraction is finished")
file.close()    
outputFile.close()

