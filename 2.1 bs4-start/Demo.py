from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8")as file:
     contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)
# print(soup.prettify())


# print(soup.p)

find_all = soup.find_all(name="a")


# print(find_all)
#
# for tag in find_all:
#      # print(tag.getText())
#      # print(tag.get("href"))


heading_1 = soup.find(name="h1", id="name")
# print(heading)
# print(heading.text)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))
# print(section_heading.text)

# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
company_url = soup.select_one(selector="p a")

# print(company_url)

# <h1 id="name">Vivek p.s</h1>
name = soup.select_one(selector="#name")
print(name)

heading = soup.select(".heading")
print(heading)

