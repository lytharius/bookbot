import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import find_words, count_characters, sort_character_counts

def main():
    num_words = find_words()
    char_count = count_characters()
    word_counts = sort_character_counts(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1], "...")
    print("----------- Word Count ----------")  
    print("Found", num_words, "total words")
    print("--------- Character Count -------") 
    print("Character counts:")
    for char, count in word_counts.items():
        print(f"{char}: {count}")

main()