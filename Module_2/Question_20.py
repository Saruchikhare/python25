def longest_word_length(word_list):
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)

    return max_length

words = ["apple", "farm", "febbles", "fortunate"]
longest_length = longest_word_length(words)
print("Length of the Longest" word, longest_length)
