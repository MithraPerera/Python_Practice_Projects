import spacy
nlp = spacy.load("en_core_web_sm")

# Exercise 1: using lemmatization in spacy

doc = nlp("running painting walking dressing likely children who good ate fishing")

for token in doc:
    print(token, "|", token.lemma_)

text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""

# Exercise 2: Using lemmatization in spacy


#step1: Creating the object for the given text

doc = nlp(text)

#step2: getting the base form for each token using spacy 'lemma_'

words = [token.lemma_ for token in doc]

#step3: joining all words in a list into string using 'join()'

print(" ".join(words))