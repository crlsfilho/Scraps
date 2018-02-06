# Import the libraries
from bs4 import BeautifulSoup
import requests
import csv
import sys

# Enconding to UTF-8.
reload(sys)
sys.setdefaultencoding('utf8')

# Extracting the source code.
url = "https://news.ycombinator.com/jobs"


# Creating a Response object from the page.
response = requests.get(url)
 
# Extracting the source code.
data = response.text
 
# Sending the code to Beautiful Soup to create an object for it.
soup = BeautifulSoup(data, 'lxml')
 
# Extracting all the tags with class 'storylink' into a list. 
titles = soup.findAll('a', {'class': 'storylink'})

 
# Extracting text from the the tags.
for title in titles:
    print(title.text)

# Create a csv file with the results.     
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	for title in titles:
		writer.writerow([title.text])
    

