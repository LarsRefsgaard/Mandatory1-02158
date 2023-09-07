import random
import string

# Define the search pattern
search_pattern = "ABCDEFDGHIJKL"

# Generate random text with minimal occurrences of the search pattern
def generate_random_text(file_size, pattern, max_pattern_occurrences):
    text = ''.join(random.choice(string.ascii_letters) for _ in range(file_size))
    pattern_occurrences = 0
    while pattern_occurrences < max_pattern_occurrences:
        position = random.randint(0, len(text) - len(pattern))
        text = text[:position] + pattern + text[position + len(pattern):]
        pattern_occurrences += 1
    return text

# Define the file size and maximum pattern occurrences
file_size = 10000000 # Adjust this to your desired file size
max_pattern_occurrences = 256  # Adjust this to control the number of pattern occurrences

# Generate random text with the search pattern
random_text = generate_random_text(file_size, search_pattern, max_pattern_occurrences)

# Save the random text as a file
with open("large_file.txt", "w") as file:
    file.write(random_text)

print("File with search pattern generated successfully.")
