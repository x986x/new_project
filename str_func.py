def capital_letters(input_string):
    return input_string.upper()

input_string = input()
result = capital_letters(input_string)

def capitalize_words(input_string):
    words = input_string.split()
    capitalize_words = [word.capitalize() for word in words]
    return ' '.join(capitalize_words)

def main():
    result = capitalize_words(input_string)
    print(result)

if __name__ == "__main__":
    main()
