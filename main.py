def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    chars = count_characters(text)
    print(chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    result = {}

    for char in text.lower():
        if char not in result:
            result[char] = 0

        result[char] += 1

    return result


main()
