alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
alphabet_length = len(alphabet)

def is_pangram(s):
    alphabet_count = {}

    for letter in s.lower():
        if letter in alphabet:
            if letter not in alphabet_count:
                alphabet_count[letter] = letter
    
    if len(alphabet_count) == 26:
        return True
    
    return False