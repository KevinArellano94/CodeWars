from to_camel_case import to_camel_case

def main():
    print(to_camel_case(""))
    print(to_camel_case("the_stealth_warrior"))
    print(to_camel_case("The-Stealth-Warrior"))
    print(to_camel_case("A-B-C"))

if __name__ == '__main__':
    main()