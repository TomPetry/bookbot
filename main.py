def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    words = count_words(frankenstein)
    print(f"{words} words found in the document")

main()