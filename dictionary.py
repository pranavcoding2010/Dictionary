from difflib import get_close_matches
import json
from webbrowser import get
data = json.load(open('dictionary.json'))
def translate (word):
    word = word.lower()
    if (word in data):
        return data [word]
    elif (len(get_close_matches(word,data.keys()))>0):
        y = input('Do you mean %s insted ? Enter y if yes and n means no'% get_close_matches(word,data.keys())[0])
        y = y.lower()  
        if (y == 'y'):
            return data [get_close_matches(word,data.keys())[0]]
        elif (y == 'n'):
            return "The word doesnt exist please double check it"
        else :
            return "We did not understand uour entry"
    else:
        return "The word dosent exist please double check it"
word = input('Enter the word =')
output = translate(word)
if type (output)==list :
    for item in output :
        print (item)
else : 
    print(output)
print('Print enter to exit')

