import string
from collections import Counter

def analyze_file(file_name):
    try:
        # Open the file and read its contents
        with open(file_name, 'r') as file:
            content = file.read()

        # Count the number of lines, words, and characters
        num_lines = content.count('\n') + 1
        words = content.split()
        num_words = len(words)
        num_characters = len(content)

        # Calculate the average word length
        total_word_length = sum(len(word) for word in words)
        average_word_length = total_word_length / num_words if num_words > 0 else 0

        # Count the most common word
        word_counts = Counter(words)
        most_common_word = word_counts.most_common(1)[0][0]

        # Print the analysis results
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
        print("Number of characters:", num_characters)
        print("Average word length:", average_word_length)
        print("Most common word:", most_common_word)

        # Write the analysis results to a new file
        with open('analysis.txt', 'w') as analysis_file:
            analysis_file.write(f"Number of lines: {num_lines}\n")
            analysis_file.write(f"Number of words: {num_words}\n")
            analysis_file.write(f"Number of characters: {num_characters}\n")
            analysis_file.write(f"Average word length: {average_word_length:.2f}\n")
            analysis_file.write(f"Most common word: {most_common_word}\n")

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", str(e))

# Ask the user to enter the name of a text file
file_name = input("Enter the name of the text file to analyze: ")
analyze_file(file_name)