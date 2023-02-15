import spacy

nlp = spacy.load("en_core_web_sm")  #creating an object and loading the pre-trained model for "English"

text = ''' Ravi and Raju are the best friends from school days.They wanted to go for a world tour and 
visit famous cities like Paris, London, Dubai, Rome etc and also they called their another friend Mohan to take part of this world tour.
They started their journey from Hyderabad and spent next 3 months travelling all the wonderful cities in the world and cherish a happy moments!
'''

# https://spacy.io/usage/linguistic-features

#creating the nlp object
doc = nlp(text)

proper_nouns = []

for token in doc:
    if token.pos_ == "PROPN":
        proper_nouns.append(token)

print(proper_nouns, f"\nCount: {len(proper_nouns)}")

text = '''The Top 5 companies in USA are Tesla, Walmart, Amazon, Microsoft, Google and the top 5 companies in 
India are Infosys, Reliance, HDFC Bank, Hindustan Unilever and Bharti Airtel'''


doc = nlp(text)

company_names = []

for ent in doc.ents:
    if ent.label_ == "ORG":
        company_names.append(ent.text)

print(f"Company Names: {company_names} \nCount: {len(company_names)}")