import nltk, re, random
from nltk.tokenize import word_tokenize
from collections import defaultdict, deque
nltk.download('punkt')

document = """
He said we gonna take over the world
One ocean at a time
He said i had a heart like gold
And a smile like the california sunshine
He called me baby loves that i had diamonds in my eyes
Pineapple sweet
Kiss me please
And on the day he said goodbye
He said ohh ohh ohh
Ill come back for you
And you ohh oh
You know my love is true
Untill that day ill be pacific blue
Pacific blue
I'm restless like the ocean waves
You pull me like the time
The roots beneath my shaded tree
The moon dancing across my sky
He whispers to me on the breeze calls on summer winds
Sweet nothing for hes baby love says hell be back again
He said ohh ohh oh
Ill come back for you
And youu oh oh
You know my love is true
Untill that day ill be pacific blue
Pacific blue
Ohhh ohhh ohh
Ohh ohh
He said ohh ohh ill come back for you
And you
You know my love is true
Untill that day ill be pacific blue
Pacific blue
"""

class MarkovChain:
  def __init__(self):
    self.lookup_dict = defaultdict(list)
    self._seeded = False
    self.__seed_me()

  def __seed_me(self, rand_seed=None):
    if self._seeded is not True:
      try:
        if rand_seed is not None:
          random.seed(rand_seed)
        else:
          random.seed()
        self._seeded = True
      except NotImplementedError:
        self._seeded = False

  def add_document(self, str):
    preprocessed_list = self._preprocess(str)
    pairs = self.__generate_tuple_keys(preprocessed_list)
    for pair in pairs:
      self.lookup_dict[pair[0]].append(pair[1])

  def _preprocess(self, str):
    cleaned = re.sub(r'\W+', ' ', str).lower()
    tokenized = word_tokenize(cleaned)
    return tokenized

  def __generate_tuple_keys(self, data):
    if len(data) < 1:
      return

    for i in range(len(data) - 1):
      yield [ data[i], data[i + 1] ]

  def generate_text(self, max_length=50):
    context = deque()
    output = []
    if len(self.lookup_dict) > 0:
      self.__seed_me(rand_seed=len(self.lookup_dict))
      chain_head = [list(self.lookup_dict)[0]]
      context.extend(chain_head)

      while len(output) < (max_length - 1):
        next_choices = self.lookup_dict[context[-1]]
        if len(next_choices) > 0:
          next_word = random.choice(next_choices)
          context.append(next_word)
          output.append(context.popleft())
        else:
          break
      output.extend(list(context))
    return " ".join(output)

my_markov = MarkovChain()
my_markov.add_document(document)
generated_text = my_markov.generate_text()
print(generated_text)
