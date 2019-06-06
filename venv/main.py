import urllib
from bs4 import BeautifulSoup
import requests
import pandas as pd


def format_html(word):
    for x in range(len(word)):
        if word[0:1] == '\n' or word[0:1] == " ":
            return format_html(word[1:])
        else:
            return word

def format_links(site_link, link):
    return (site_link + link)

def get_indeed():
    indeed = requests.get("https://www.indeed.ca/jobs?q=software+co-op&l=Toronto")
    print(indeed)

    soup = BeautifulSoup(indeed.content, 'html.parser')

    jobs_column = soup.find(id='resultsCol')

    job_names_container = jobs_column.select("#resultsCol .jobsearch-SerpJobCard .title a.jobtitle")
    job_names = [name.get_text() for name in job_names_container]

    job_companies_container = jobs_column.select("#resultsCol .jobsearch-SerpJobCard .sjcl span.company")
    job_companies = [company.get_text() for company in job_companies_container]

    job_location_container = jobs_column.select("#resultsCol .jobsearch-SerpJobCard .sjcl .location")
    job_location = [location.get_text() for location in job_location_container]

    job_description_container = jobs_column.select("#resultsCol .jobsearch-SerpJobCard .summary")
    job_description = [description.get_text() for description in job_description_container]

    job_links_container = jobs_column.select("#resultsCol .jobsearch-SerpJobCard .title a[href]")
    job_links = [links.get("href") for links in job_links_container]

    for x in range(len(job_names)):
        job_names[x] = format_html(job_names[x])
        job_companies[x] = format_html(job_companies[x])
        job_location[x] = format_html(job_location[x])
        job_description[x] = format_html(job_description[x])
        job_links[x] = format_links("https://www.indeed.ca", job_links[x])


    job = pd.DataFrame({
        "job_names": job_names,
        "job_companies": job_companies,
        "job_locations": job_location,
        "job_description": job_description,
        "job_links": job_links
    })
    pd.set_option('display.max_colwidth', -1)

    print(job)


def main():
    get_indeed()

if __name__== "__main__":
    main()
