# Import requests module
import requests
from datetime import datetime
import time

# Get the time now
now = datetime.now()
dt_string = now.strftime("%d-%b %H:%M:%S")

# user input website of their choice
url = input('Enter a url:')
time.sleep(0.5)
print('\n  Target url:',url)
print('Time started:', dt_string)

# print the full page
r = requests.get(url)
print("\nGetting request...")
time.sleep(2)
print('\n',r.text)

# print the status code
print("\nStatus code:")
print("\t *",r.status_code)
time.sleep(2)

# printing the header
h = requests.head(url)
print ("\nHeader:")
print("**********")

# to print line by line
for x in h.headers:
    print("\t",x,".",h.headers[x])
print("**********")

# modify the headers user-agent
