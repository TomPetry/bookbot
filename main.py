from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(file_path):
    frankenstein = get_book_text(file_path)
    num_words = get_num_words(frankenstein)
    letters = get_num_chars(frankenstein)
    sorted_letters = sort_and_restructure(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for letter in sorted_letters:
        print(f"{letter['char']}: {letter['num']}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])



main()