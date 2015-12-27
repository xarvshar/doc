from bs4 import BeautifulSoup
soup = BeautifulSoup(open("red.html"),'html.parser')
print(soup.h1.text)
print(soup.find_all("p","clinic-timings-day"))
print(soup.find_all("p","clinic-timings-session"))
print(soup.find_all("p","doctor-qualifications"))
for links in (soup.find_all("h2","doctor-specialties")):
    print(links.text)
for recom in (soup.find_all("p","recomend")):
    print(recom.text)
print(soup.find(itemprop="streetAddress").string)
for link in (soup.find_all("span","clinic-fees-mobile-indicator")):
    print(link.p)
    print(link.find(style="color:#B1B1B1").string)
