import sys
def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def find_words():
    text = get_book_text()
    words = text.split()
    return len(words)

def count_characters():
    text = get_book_text().lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1    
    
    return char_count

def sort_character_counts(char_count):
    return dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))