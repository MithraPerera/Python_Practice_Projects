import spacy

nlp = spacy.blank("en")
text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

# TODO: Write code here
# Hint: token has an attribute that can be used to detect a url

doc = nlp(text)

urls = [token for token in doc if token.like_url]
print(urls)

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"

# TODO: Write code here
# Hint: Use token.i for the index of a token and token.is_currency for currency symbol detection

doc = nlp(transactions)
currency = [token.text for token in doc if token.is_currency or token.like_num]
print(" ".join(currency[:2]))
print(" ".join(currency[2:4]))