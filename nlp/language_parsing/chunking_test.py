from nltk import RegexpParser, Tree

# define chunk grammar to chunk an entire sentence together
grammar = "Chunk: {<.*>+}"

# create RegexpParser object
parser = RegexpParser(grammar)

text = "The quick brown fox jumps over the lazy dog."


for each_word in text:
    print(each_word)
    # pos_tagged_oz.append(pos_tag(each_word))

# chunk the pos-tagged sentence at index 230 in pos_tagged_oz
# chunked_dancers = parser.parse()
# print(chunked_dancers)

# define noun phrase chunk grammar using chunk filtering here



# create RegexpParser object here


# chunk and filter the pos-tagged sentence at index 230 in pos_tagged_oz here



# pretty_print the chunked and filtered sentence here
# Tree.fromstring(str(filtered_dancers)).pretty_print()
