from bs4 import BeautifulSoup
import requests

# Copies the html code of the given URL
html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Web+Development&txtLocation=').text

soup = BeautifulSoup(html_file, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    job_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
    skills = job.find('span', class_='srp-skills').text.replace(' ', '')
    location = job.find('ul', class_='top-jd-dtl clearfix').span.text.replace(' ', '')
    more_info = job.header.h2.a['href']
    print(f'Çompany name : {job_name.strip()}')
    print(f'Key skills : {skills.strip()}')
    print(f'Location : {location}')
    print(f'More info : {more_info}')
    print('')
