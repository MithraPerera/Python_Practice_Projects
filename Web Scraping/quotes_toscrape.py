import requests
import bs4

i = 1
authors = set()
quotes = set()
top_tags = set()

while True:
    # Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ and get the HMTL text from the homepage.
    try:
        result = requests.get(f"http://quotes.toscrape.com/page/{i}")
    except:
        print("Error.")
    else:
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        if "No quotes found!" in str(soup):
            break
        # Get the names of all the authors without duplicates
        for name in [author.text for author in soup.select(".author")]:
            authors.add(name)
        # Create a list of all the quotes without duplicates
        for quote in [quotes.text for quotes in soup.select(".quote > .text")]:
            quotes.add(quote)
        # extract the top ten tags from the requests text shown on the top right from the home page
        # HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.
        for tag in [tag.text for tag in soup.select(".tag-item > .tag")]:
            top_tags.add(tag)
        #top_tags = top_tags + [tag.getText() for tag in soup.select(".tag-item > .tag")]
    i += 1

print(i)
print(authors)
# print(quotes)
# print(top_tags)
