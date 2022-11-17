import spacy
from nltk import Tree
# from squids import squids_text

squids_text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

dependency_parser = spacy.load('en_core_web_sm')

parsed_squids = dependency_parser(squids_text)

# Assign my_sentence a new value:
my_sentence = "Your sentence goes here!"
my_sentence = "The quick brown fox jumps over the lazy dog."
my_parsed_sentence = dependency_parser(my_sentence)

def to_nltk_tree(node):
  if node.n_lefts + node.n_rights > 0:
    parsed_child_nodes = [to_nltk_tree(child) for child in node.children]
    return Tree(node.orth_, parsed_child_nodes)
  else:
    return node.orth_

for sent in parsed_squids.sents:
  to_nltk_tree(sent.root).pretty_print()

for sent in my_parsed_sentence.sents:
 to_nltk_tree(sent.root).pretty_print()
