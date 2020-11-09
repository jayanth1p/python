import json 
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("did you mean %s?.enter Y if yes and N if no: "% get_close_matches(w,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "the word does not exist , please double check."
        else:
            return "we didn't understand your entry"
    else:
        return "the word does not exist , please double check."
word = input("enter word: ")
output = translate(word)


if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

