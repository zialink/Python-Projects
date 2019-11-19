import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def translate(word):
    if (word in data):
        return data[word]
    elif(word.upper() in data):
        return data[word.upper()]
        word = word.lower()
        if (word in data):
            return data[word]
        elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0 :
            confirm= input("Did you mean %s instead? Type y for yes and n for no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
            if confirm == "y":
                word = get_close_matches(word, data.keys(), cutoff=0.8)[0]
                return data[word]
            else:
                word= input("This word does not exist. Check the word and try again: ")
                return data[word]
        else:
            word= input("This word does not exist. Check the word and try again: ")
            return data[word]

word= input("Enter a word: ")
dict = translate(word)
for d in dict:
    print(d)
