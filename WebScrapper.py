import requests
import bs4

#Grabbing a TITLE 
print(" GRABBING A TITLE \n")
result = requests.get("https://en.wikipedia.org/wiki/Harry_Potter_(film_series)")
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup.select('title'))

#Grabbing a CLASS
print("\n GRABBING A CLASS \n")
result = requests.get("https://en.wikipedia.org/wiki/Harry_Potter_(film_series)")
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup.select('.firstHeading'))

#Grabbing an ID
print("\n GRABBING AN ID \n")
print(soup.select('#firstHeading'))

#Grabbing a IMAGE
print("\n GRABBING A IMAGE \n")
req = requests.get("https://www.google.com/search?q=marine&rlz=1C1CHBF_enIN913IN913&sxsrf=ALeKk02jPd_IQaalR_bDofnADfE6wH2SLA:1608824399832&source=lnms&tbm=isch&sa=X&ved=2ahUKEwisg-72-ebtAhVSwjgGHb04CLsQ_AUoAXoECBMQAw&biw=1536&bih=760")
soup = bs4.BeautifulSoup(req.text,'lxml')
print(soup.select('.t0fcAb')[0])


#Working with multiple pages and items
base_url = 'http://books.toscrap.com/catalogue/page-{}.html'
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
