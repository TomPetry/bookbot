from stats import *


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    words = get_num_words(frankenstein)
    letters = get_num_chars(frankenstein)
    print(f"{words} words found in the document")
    print(letters)

main()