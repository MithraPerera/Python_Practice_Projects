import requests
import bs4

# Get Website
try:
    result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
except:
    print("Error.")
else:
    print("Successful.")

# Use beautiful soup to parse it into a readable format
soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)

# Print Title of Web Page
site_title = soup.select("title")
# print(site_title[0].getText())

# Print Table of Contents
table_of_contents = soup.select(".vector-toc-text")
# for item in table_of_contents:
# print(item.text)

# Get an Image
img = soup.select(".image > img")
print(img[0]['src'])
