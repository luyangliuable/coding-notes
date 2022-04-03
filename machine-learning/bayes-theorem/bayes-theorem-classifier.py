from reviews import neg_list, pos_list, neg_counter, pos_counter

print(len(pos_list))
print(len(neg_list))
total_reviews = len(pos_list) + len(neg_list)
print(total_reviews)

percent_pos = len(pos_list)/total_reviews
percent_neg = len(neg_list)/total_reviews

print(percent_pos)
print(percent_neg)
