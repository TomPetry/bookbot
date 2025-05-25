def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    letters = {}
    for char in text:
        letter = char.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters