import string
import re #regular expression
from nltk.corpus import stopwords #$ pip install nltk

#uncomment following 2 lines to download NLTK stopwords data
#import nltk
#nltk.download()

#remove all punctuation
def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    return text.strip(' ')

#removes URLs
def removes_url(text):
    text = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', text)
    return text.strip(' ')

#removes stop-words
def remove_stopwords(text):
    StopWords = stopwords.words("english")
    final = ' '.join([word for word in text.split() if word not in StopWords])
    return final.strip(' ')

#removes # and @ in the beginning of each word. ex: #Good -> Good
def remove_hashtag(text):
    new_text = ""
    for words in text.split():
        if words.startswith('#') or words.startswith('@'): #remove @ amd #
            new_text += words[1:]
            new_text += ' '
        else:
            new_text += words
            new_text += ' '
    return new_text.strip(' ')

#removes # and @ even between words. ex: #life#is#good -> life is good
def remove_hash_symbol(text):
    to_be_removed = ['#', '@']
    for prohibited_symbol in to_be_removed:
        text = text.replace(prohibited_symbol, ' ')
    text = ' '.join(text.split())
    return text.strip(' ')

print(remove_punctuation("Helloooo@@@@!!!!! How come... no way! xD"))
print(removes_url("www.google.com https://abola.pt abc@xyz.com"))
print(remove_stopwords("Hi, my name is Son-Goku and I'm a super saiyan"))
print(remove_hashtag("hahah, #sqn, #life #is #good, #go#go#go"))
print(remove_hash_symbol("hahah, #sqn, #life #is #good, #go#go#go"))
print(remove_hash_symbol("abc@xyz.com, @Paul, @HTC"))
