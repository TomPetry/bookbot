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

def sort_and_restructure(letters):
    sort_dicts = []
    for letter in letters:

        if not letter.isalpha():
            continue

        sort_dicts.append({
            "char": letter,
            "num": letters[letter]
        })

    sort_dicts.sort(reverse=True, key=sort_on)

    return sort_dicts

def sort_on(dict):
    return dict["num"]