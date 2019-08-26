from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import pandas as pd


def format_html(word):
    for x in range(len(word)):
        if word[0:1] == '\n':
            return format_html(word[1:])
        elif word[0:1] == " ":
            return format_html(word[1:])
        else:
            return word

def format_links(site_link, link):
    return (site_link + link)


#File for all scraped data functions

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

    return job


def get_glassdoor():

    url = "https://www.glassdoor.ca/Job/software-intern-jobs-SRCH_KO0,15.htm"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    glassdoor = urlopen(req).read()

    if(glassdoor):
        print("Glassdoor: 200")


    page_soup = BeautifulSoup(glassdoor, 'html.parser')

    jobs_column = page_soup.find(id='JobResults')

    job_names_container = jobs_column.select(".jl .jobContainer > a.jobLink.jobInfoItem.jobTitle ")
    job_names = [name.get_text() for name in job_names_container]

    job_companies_container = jobs_column.select(".jl .jobContainer .jobHeader a div.jobInfoItem")
    job_companies = [company.get_text() for company in job_companies_container]

    job_location_container = jobs_column.select(".jl .jobContainer .jobInfoItem span.subtle")
    job_location = [location.get_text() for location in job_location_container]

    job_description = []
    for i in range(len(job_location_container)):
        job_description.append("Not Available")

    job_links_container = jobs_column.select(".jl .jobContainer .jobHeader a[href]")
    job_links = [links.get("href") for links in job_links_container]

    print(len(job_names))
    print(len(job_links))

    for x in range(len(job_names)):
        job_names[x] = format_html(job_names[x])
        job_companies[x] = format_html(job_companies[x])
        job_location[x] = format_html(job_location[x])
        job_description[x] = format_html(job_description[x])
        job_links[x] = format_links("https://www.glassdoor.ca", job_links[x])


    job = pd.DataFrame({
        "job_names": job_names,
        "job_companies": job_companies,
        "job_locations": job_location,
        "job_description": job_description,
        "job_links": job_links
    })
    pd.set_option('display.max_colwidth', -1)

    return job