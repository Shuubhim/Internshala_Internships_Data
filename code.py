import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

roles = []
name = []
stipends = []
location = []
duration = []


for j in range(0,200):
  web_page = requests.get('https://internshala.com/internships/page{}'.format(i))
  soup = BeautifulSoup(web_page.text, 'lxml')
  company = soup.find('div', id ='internship_list_container_1')

  

  for i in range(50):
      try:
          roles.append(company.findAll('h3', class_='job-internship-name')[i].text.strip())
      except (IndexError, AttributeError):
          roles.append(np.nan)

      try:
          name.append(company.findAll('p', class_='company-name')[i].text.strip())
      except (IndexError, AttributeError):
          name.append(np.nan)

      try:
          stipends.append(company.findAll('span', class_='stipend')[i].text.strip())
      except (IndexError, AttributeError):
          stipends.append(np.nan)

      try:
          duration.append(company.select(".row-1-item .ic-16-calendar + span")[i].text.strip())
      except (IndexError, AttributeError):
          duration.append(np.nan)

      try:
          location.append(company.select(".ic-16-map-pin + span")[i].text.strip())
      except (IndexError, AttributeError):
          location.append(np.nan)

df = pd.DataFrame({'Role': roles, 'Company': name, 'Stipend': stipends,
                   'Duration': duration, 'Location': location})
df.shape
df.isnull().sum()
df.describe()
df .sample(5)
