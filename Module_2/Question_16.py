#16 Write a Python program to count the occurrences of each word in a given sentence

def count_word_occurrences(sentence):
    words = sentence.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(words, 0) + 1

    return word_counts

input_sentence = input("Enter a sentence: ")
word_occurances = count_word_occurrences(input_sentence)

print("Word occurrences:")
for word, count in count_word_occurrences.items():
    print(f"'{word}': {count}")
