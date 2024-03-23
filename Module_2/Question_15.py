#15 Write a Python program to count occurrences of a substring in a string.

def count_word_occurances(sentence):
    words = sentence.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] = +1

        else:
            word_counts[word] = 1

    return word_counts

input_sentence = input("Enter a Sentence: ")
word_occurances =  count_word_occurances(input_sentence)
print("word_occurances:")
print(word_occurances)