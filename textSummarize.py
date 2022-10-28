import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger')
ex = "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."
# Doing Tokenization and POS Tagging.
def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    print("The RESULT OF TOKENIZATION IS : ")
    print(sent)
    print() 
    print()
    sent = nltk.pos_tag(sent)
    print(sent)
    return sent

sent = preprocess(ex)
# NN	noun, singular (cat, tree)
# JJ	This NLTK POS Tag is an adjective (large)
pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
# print(cs)

# Parsing the Tree.
from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint
iob_tagged = tree2conlltags(cs)
# pprint(iob_tagged)
listOfEntities = list()
for i in iob_tagged:
    if ((i[1]=='NNP') or (i[1]=='NN') ):
        listOfEntities.append(i[0])

# Removing the dublicates from list of entities 
listOfEntities = list(dict.fromkeys(listOfEntities))
print(listOfEntities)