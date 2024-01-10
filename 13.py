'''Write a program to compute the frequency of the words from the input. The
output should output after sorting the key alphanumerically.'''

def compute_word_frequency(input_text):
    word_frequency = {}

    # Splitting the input text into words
    words = input_text.split()

    # Counting the frequency of each word
    for word in words:
        word = word.lower()  # Convert to lowercase to treat words case-insensitively
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Sorting the keys alphanumerically
    sorted_word_frequency = dict(sorted(word_frequency.items()))

    return sorted_word_frequency

# Example usage:
input_text = input("Enter a sentence or text: ")
result = compute_word_frequency(input_text)

# Displaying the frequency of words after sorting the keys
print("\nWord Frequency (Alphanumerically Sorted):")
for word, frequency in result.items():
    print(f"{word}: {frequency}")
