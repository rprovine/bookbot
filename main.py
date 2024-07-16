# Read contents of file and store in variable
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents  # Moved return statement outside the with block

# Take text and split into words
def split_text(text):
    return text.split()

# Count the number of words in the text
def count_words(text):
    words = split_text(text)  # Split the text into words before counting
    return len(words)

# Take the text as a string and return the number of times each character appears using a dictionary. Convert to lowercase with no duplicates without using a set.
def count_characters(text):
    character_count = {}
    for character in text.lower():
        if character.isalpha():  # Check if character is alphabetic
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def sort_characters(dictionary):
    return sorted(dictionary.items(), key=lambda x: x[0])

def print_report(word_count, sorted_characters):
    print(f"Word Count: {word_count}")  # Print word count
    print("Character Counts:")
    for item in sorted_characters:
        print(f"Character: '{item[0]}' - Count: {item[1]}")  # Print each character count

# Execute the program
file_contents = main()
word_count = count_words(file_contents)
dictionary = count_characters(file_contents)
sorted_characters = sort_characters(dictionary)

# Print the report
print_report(word_count, sorted_characters)