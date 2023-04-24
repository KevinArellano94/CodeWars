def xo(s):
    x_and_o = {
        "x": 0,
        "o": 0
    }

    for letter in s.lower():
        for key, value in x_and_o.items():
            if letter == key:
                value += 1
                x_and_o.update({ key: value })
    
    if x_and_o.get("x") != x_and_o.get("o"):
        return False

    return True