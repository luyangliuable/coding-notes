from reviews import neg_counter, pos_counter

# Import the `neg_counter` and `pos_counter` dictionaries from the `reviews` module.
from reviews import neg_counter, pos_counter

# Define a review that needs to be analyzed for sentiment.
review = "This cribb was amazing"

# Initialize the probabilities for positive and negative sentiments to 0.5.
percent_pos = 0.5
percent_neg = 0.5

# Calculate the total number of positive and negative words in the respective counters.
total_pos = sum(pos_counter.values())
total_neg = sum(neg_counter.values())

# Initialize the probabilities for positive and negative sentiments.
pos_probability = 1
neg_probability = 1

# Split the review into individual words.
review_words = review.split()

# Calculate the probabilities of the review being positive and negative.
for word in review_words:
  # Retrieve the frequency of the word in the positive and negative counters.
  word_in_pos = pos_counter.get(word, 0)
  word_in_neg = neg_counter.get(word, 0)
  
  # Update the probabilities based on the frequency of the word in the counters.
  pos_probability *= (word_in_pos + 1) / (total_pos + len(pos_counter))
  neg_probability *= (word_in_neg + 1) / (total_neg + len(neg_counter))
  
# Print the probabilities of the review being positive and negative.
print(pos_probability)
print(neg_probability)
