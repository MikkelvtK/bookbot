def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    char_count = count_characters(text)
    display_report(word_count, char_count, path)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    result = {}

    for char in text.lower():
        if char.isalpha():
            if char not in result:
                result[char] = 0

            result[char] += 1

    return result


def sort_chars(chars):
    return sorted(chars)


def display_report(word_count, char_count, path):
    print(f"----- Report of {path} -----")
    print(f"Number of words in the book: {word_count}")
    print()
    display_characters(char_count)


def display_characters(char_count):
    for char in sort_chars(char_count):
        print(f"The '{char}' character was found {char_count[char]} times")


main()
