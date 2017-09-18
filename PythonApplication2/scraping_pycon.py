from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("http://2015.pycon-au.org/")
html_string = driver.page_source
driver.close()

soup = BeautifulSoup(html_string, "html.parser")
links = [item.get('href') for item in soup.select("div.owl-item a")]
links.pop()

f = open('sponsors.txt','w')
for link in links:
    f.write(link + '\n')
f.close()
