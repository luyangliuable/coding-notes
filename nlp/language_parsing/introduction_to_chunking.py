from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz

sentence = "The quick brown fox jumps over the lazy dog."

# define adjective-noun chunk grammar here
chunk_grammar = "AN: {<JJ><NN>}"


# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)


# chunk the pos-tagged sentence at index 282 in pos_tagged_oz here
chunked = chunk_parser.parse(pos_tagged_oz[282])
print(pos_tagged_oz[282])
print(chunked)
scaredy_cat = chunked


# pretty_print the chunked sentence here
Tree.fromstring(str(scaredy_cat)).pretty_print()
