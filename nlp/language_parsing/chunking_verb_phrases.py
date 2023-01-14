from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from vp_chunk_counter import vp_chunk_counter

# define verb phrase chunk grammar here
"""
VP - User defined name of the chunk grammar
<VB.*> - match any verb (VB, VBD for past tense or VBN for past participle)
<DT>?<JJ>*<NN> - matches any noun phrase
<RB.?> - matches any adverb using . as wildercard and optional identifier to match 0 or 1 occurence of any character. This ensures match any form of adverb (RB, RBR, RBS)
"""
chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"

# update grammer to find verb phrase followed by noun phrase then a verb finally an optional adverb
chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"
"""
<DT>?<JJ>*<NN> - matches any noun phrase
VP - User defined name of the chunk grammar
<VB.*> - match any verb (VB, VBD for past tense or VBN for past participle)
<RB.?> - matches any adverb using . as wildercard and optional identifier to match 0 or 1 occurence of any character. This ensures match any form of adverb (RB, RBR, RBS)
? - Optional identifier meaning the adverb is optional
"""

# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)

# create a list to hold verb-phrase chunked sentences
vp_chunked_oz = list()

# create for loop through each pos-tagged sentence in pos_tagged_oz here
for pos_tagged_sentence in pos_tagged_oz:
    # chunk each sentence and append to vp_chunked_oz here
    vp_chunked_oz.append(chunk_parser.parse(pos_tagged_sentence))


# Return the 30 most common chunks
most_common_vp_chunks = vp_chunk_counter(vp_chunked_oz)


# store and print the most common vp-chunks here
print(most_common_vp_chunks)
