def subsample_frequent_words(word_count_dict, threshold=1e-5):
    total_count = sum(word_count_dict.values())
    keep_prob_dict = {}
    for word, count in word_count_dict.items():
      f = count / total_count
      keep_prob = (threshold / f) ** 0.5
      keep_prob_dict[word] = keep_prob
    return keep_prob_dict

def get_negative_sampling_prob(word_count_dict):
    adj_counts = {words: counts**0.75 for words, counts in word_count_dict.items()}
    total_frequency = sum(adj_counts.values())
    negative_sampling_prob_dict = {
        words: adj_count / total_frequency for words, adj_count in adj_counts.items()
    }
    return negative_sampling_prob_dict