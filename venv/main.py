import urllib
from bs4 import BeautifulSoup

import requests

def format_html(word):
    for x in range(len(word)):
        if word[0:1] == '\n' or word[0:1] == " ":
            return format_html(word[1:])
        else:
            return word


indeed = requests.get("https://www.indeed.ca/jobs?q=software+co-op&l=Toronto")
print(indeed)

soup = BeautifulSoup(indeed.content, 'html.parser')
#print(soup.prettify())
jobs_column = soup.find(id='resultsCol')

job_names_container = jobs_column.select("#resultsCol .jobsearch-SerpJobCard .title a")

job_names = [name.get_text() for name in job_names_container]

for name in job_names:
    name = format_html(name)
    print(name)




#print(soup.find_all(class_="title2font"))
#tags = [tag.get_text() for tag in title_tags]
#print(tags)