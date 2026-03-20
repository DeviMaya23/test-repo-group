#Question 4 Solution:
#Program: Sentence Analyzer
# This program asks the user to enter a sentence and then:
#  Counts the total number of words
# Finds the longest word in the sentence
# Displays the sentence in different formats

# Keep asking until the user enters a valid sentence
while True:
    sentence = input("Enter a sentence: ").strip()
    
    # Check if the input is empty or only spaces
    if sentence == "":
        print("Please enter a sentence.\n")
        continue
    
    # Check if the input contains at least one letter (not just numbers/symbols)
    if not any(char.isalpha() for char in sentence):
        print("Please enter a valid sentence (not just numbers).\n")
        continue
    
    # If input is valid, exit the loop
    break

# Split the sentence into individual words
words = sentence.split()

# Count how many words are in the sentence
total_words = len(words)

# Find the longest word in the sentence
longest_word = ""
for word in words:
    # Remove common punctuation from the word before checking length
    clean_word = word.strip(".,!?;:")
    
    # Update longest_word if current word is longer
    if len(clean_word) > len(longest_word):
        longest_word = clean_word

# Display the results
print("\n Results ")

# Show total number of words
print(f"Total words: {total_words}")

# Show the longest word and its length
print(f"Longest word: {longest_word} ({len(longest_word)} letters)")

# Display different versions of the sentence
print("\nSentence formats:")

# Convert all characters to uppercase
print(f"Uppercase: {sentence.upper()}")

# Convert all characters to lowercase
print(f"Lowercase: {sentence.lower()}")

# Capitalize the first letter of each word
print(f"Title case: {sentence.title()}")

# Reverse the entire sentence
print(f"Reversed: {sentence[::-1]}")