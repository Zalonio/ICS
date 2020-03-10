import requests
from bs4 import BeautifulSoup

URL = "https://ca.news.search.yahoo.com/search;_ylt=AwrC0F.EMFVeZGoATyjwFAx.;_ylc=X1MDMjExNDcyMTAwOARfcgMyBGZyA3lmcC10BGdwcmlkA1lGVU9zVnRwUWsycFJ2cTZySE5kaEEEbl9yc2x0AzAEbl9zdWdnAzEEb3JpZ2luA2NhLm5ld3Muc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAwRxc3RybAMyNARxdWVyeQNibGl6emFyZCUyMGVudGVydGFpbm1lbnQEdF9zdG1wAzE1ODI2NDEzNjE-?p=blizzard+entertainment&fr2=sb-top-ca.news.search&fr=yfp-t"

#URL = "https://www.google.com/search?q=blizzard+entertainment&source=lmns&tbm=nws&bih=854&biw=1200&safe=strict&hl=en-US&ved=2ahUKEwj4pun-kPznAhUYzKwKHeaeCHAQ_AUoAXoECAEQAQ"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#results = soup.findAll("div", {"class": "dd NewsArticle"})
#soup.find_all('div', class_=['dd NewsArticle'])

results = soup.find(id='yui_3_10_0_1_1583244690748_303')

#code_elems = soup.findAll("li", {"class": "first"})
#code_elems = soup.findAll("div", {"id": "web"})
#code_elems = soup.findAll("div", {"id": "dd NewsArticle"})
code_elems = soup.findAll("ol", {"id": "yui_3_10_0_1_1583244690748_302"})
#results = soup.find(class="gG0TJc")
#results = soup.findAll("div", {"class": "gG0TJc"})

# Look for Python jobs
# python_jobs = results.find_all(id='yUnivHead')

#print(results.prettify)
#print(results.prettify())

print(code_elems)

#print(code_elems)

"""
for code_elem in code_elems:
  title_elem = code_elem.find('h4', class_='fz-16 lh-20', title_=())
  #title_elem = job_elem.find('h2', class_='title')
  description_elem = code_elem.find('p', class_='yui_3_10_0_1_1583244690748_297')
  date_elem = code_elem.find('span', class_='fc-2nd mr-8')

#print(title_elem)
print(title_elem.text.strip())
print(description_elem)
print(date_elem.text.strip())
print()

#A massiv emilestone really, really achieved irghthtis minute, no more diddly daddling, full gps trackign systm or somethign heavy within a day, we must anchor those expectations heavily upone everyday
#lackingsophisticated wordings, my thoughts..

#Amazing brimming feelings... the translucent planes of reality extending, mind really only permeates for one day 
#When you lay foundationf or stiving paintings, amazing...abs#No, no rmember sinon,mkae a sconcious effort than thos ewho dilly dally, they are falsehoods
"""
"""
"""
"""
for p_job in python_jobs:
    link = p_job.find("a")["href"]
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

# Print out all available jobs from the scraped webpage
job_elems = results.find_all("section", class_="card-content")
for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
"""