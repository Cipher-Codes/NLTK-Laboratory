import nltk

def tokenize(sent):
    tokens = nltk.word_tokenize(sent)
    return tokens


sentence = [
    "I'm Currently Pursuing my Under Graduate Degree",
    "Hello Jeyesh this will make my day special",
    "Stay happy rule the sadness with your smile",
    "Start accepting things"
    ]

for i in sentence:
    hel = tokenize(i)
    print(hel)
