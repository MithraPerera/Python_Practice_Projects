import requests
import bs4

# Get title of every book with 2 stars

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
two_star_books = []

for i in range(1, 51):
    url = base_url.format(i)
    try:
        result = requests.get(url)
    except:
        print("Error.")
    else:
        soup = bs4.BeautifulSoup(result.text, "lxml")
        products = soup.select(".product_pod")
        for product in products:
            if len(product.select(".star-rating.Two")) != 0:
                two_star_books.append(product.select("a")[1]["title"])

print(len(two_star_books))