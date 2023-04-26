def to_camel_case(text):
    delimiter = ['-', '_']
    camel_case_string = []
    capitalize_letter = False

    for letter in text:
        camel_case_string.append(letter)

        if capitalize_letter == True:
            camel_case_string.pop()
            camel_case_string.append(letter.upper())
            capitalize_letter = False

        if letter in delimiter:
            camel_case_string.pop()
            capitalize_letter = True

    return ''.join(word[0] for word in camel_case_string)