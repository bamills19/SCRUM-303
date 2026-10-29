
word = "whatever"
def has_duplicate_letters(word):
    seen_letters = []
    for letter in list(word):
        if letter in seen_letters:
            return True
    else:
        seen_letters.append(letter)
    return False