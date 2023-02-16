import spacy

nlp = spacy.load("en_core_web_sm")

# Exercise 1: Extract all the Geographical (cities, Countries, states) names from a given text

text = """Kiran want to know the famous foods in each state of India. So, he opened Google and search for this question. Google showed that
in Delhi it is Chaat, in Gujarat it is Dal Dhokli, in Tamilnadu it is Pongal, in Andhrapradesh it is Biryani, in Assam it is Papaya Khar,
in Bihar it is Litti Chowkha and so on for all other states"""

doc = nlp(text)

locations = []

for ent in doc.ents:
    if ent.label_ == "GPE":
        locations.append(ent.text)

print(locations)
print(f"Count: {len(locations)}")

# Exercise 2: Extract all the birth dates of cricketers in the given Text

text = """Sachin Tendulkar was born on 24 April 1973, Virat Kholi was born on 5 November 1988, Dhoni was born on 7 July 1981
and finally Ricky ponting was born on 19 December 1974."""

doc = nlp(text)

birthdays = []

for ent in doc.ents:
    if ent.label_ == "DATE":
        birthdays.append(ent.text)

print(birthdays)
print(f"Count: {len(birthdays)}")