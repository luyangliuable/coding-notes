from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from np_chunk_counter import np_chunk_counter

# define noun-phrase chunk grammar here
"""
    NP - a user defined name for the chunk
    <DT> - maches determiner
    ? - means optional ( 0 or 1 )
    <JJ> - matches adjective
    * - called a Kleene star, matches 0 or more occurences
"""
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)


# create a list to hold noun-phrase chunked sentences
np_chunked_oz = list()

# create a for-loop through each pos-tagged sentence in pos_tagged_oz here
for pos_tagged_sentence in pos_tagged_oz:
  # chunk each sentence and append to np_chunked_oz here
  np_chunked_oz.append(chunk_parser.parse(pos_tagged_sentence))


most_common_np_chunks = np_chunk_counter(np_chunked_oz)


# store and print the most common np-chunks here
print(most_common_np_chunks)
