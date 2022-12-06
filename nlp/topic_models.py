import nltk, re
# from sherlock_holmes import bohemia_ch1, bohemia_ch2, bohemia_ch3, boscombe_ch1, boscombe_ch2, boscombe_ch3
# from preprocessing import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# preparing the text
# corpus = [bohemia_ch1, bohemia_ch2, bohemia_ch3, boscombe_ch1, boscombe_ch2, boscombe_ch3]
# preprocessed_corpus = [preprocess_text(chapter) for chapter in corpus]

# Update stop_list:
stop_list = ['the', 'know', 'five', 'fifity', 'rice', 'within', 'self', 'across', 'see', 'one']
# filtering topics for stop words

def filter_out_stop_words(sentence):
    no_stops_sentence = []
    no_stops_chapter = [word for word in sentence.split(" ") if word not in stop_list]
    no_stops_sentence.append(no_stops_chapter)
    return no_stops_sentence[0]


sentence = "The quick brown fox jumps over the lazy dog."
filtered_for_stops = filter_out_stop_words(sentence)
print(filtered_for_stops)

# creating the bag of words model
bag_of_words_creator = CountVectorizer()
bag_of_words = bag_of_words_creator.fit_transform(filtered_for_stops)

# Count
cv = CountVectorizer()
word_count_vector = cv.fit_transform(filtered_for_stops)
print(word_count_vector.shape)
print(word_count_vector)

# creating the tf-idf model
# tfidf_creator = TfidfVectorizer(min_df = 0.2)
tfidf_creator = TfidfVectorizer(smooth_idf=True, use_idf=True)
tfidf = tfidf_creator.fit_transform(word_count_vector)

# # creating the bag of words LDA model
# lda_bag_of_words_creator = LatentDirichletAllocation(learning_method='online', n_components=10)
# lda_bag_of_words = lda_bag_of_words_creator.fit_transform(bag_of_words)

# # creating the tf-idf LDA model
# lda_tfidf_creator = LatentDirichletAllocation(learning_method='online', n_components=10)
# lda_tfidf = lda_tfidf_creator.fit_transform(tfidf)

# print("~~~ Topics found by bag of words LDA ~~~")
# for topic_id, topic in enumerate(lda_bag_of_words_creator.components_):
#   message = "Topic #{}: ".format(topic_id + 1)
#   message += " ".join([bag_of_words_creator.get_feature_names()[i] for i in topic.argsort()[:-5 :-1]])
#   print(message)

# print("\n\n~~~ Topics found by tf-idf LDA ~~~")
# for topic_id, topic in enumerate(lda_tfidf_creator.components_):
#   message = "Topic #{}: ".format(topic_id + 1)
#   message += " ".join([tfidf_creator.get_feature_names()[i] for i in topic.argsort()[:-5 :-1]])
#   print(message)