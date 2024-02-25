from bs4 import BeautifulSoup
import requests
import pandas as pd

from Learning_Module2.Home_works.Home_15.scraping.BeatifulSoup.JobElement import JobElement
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71'}
url = "https://realpython.github.io/fake-jobs/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
print("soup", soup.text)

container = soup.find(id='ResultsContainer')
div_jobs_list = container.find_all("div", class_='card-content')
object_job_list =[]
index = 0
for element in div_jobs_list:
    index = index+1
    title = element.find_all(True, {'class': "title is-5"})
    subtitle = element.find_all(True, {'class': "subtitle is-6 company"})
    location = element.find_all(True, {'class': "location"})
    date = element.find_all(True, {'class': 'is-small has-text-grey'})

    jobElement = JobElement(title=title, subtitle=subtitle, location=location, date=date, job_id=index)
    object_job_list.append(jobElement)

df_bs = pd.DataFrame(object_job_list)
print("df_  :",df_bs.to_string())
df_bs.to_csv('jobs.csv')
