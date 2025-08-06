from stats import count_words, count_characters
from sys import argv, exit

if len(argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
else:
    def get_book_text(path_to_file):
        with open(path_to_file, "r") as f:
            file_contents = f.read()
            return file_contents

    def main(file_path):
        file_text = get_book_text(file_path)
        print(file_text)

    count_words(get_book_text(argv[1]))
    count_characters(get_book_text(argv[1]))


# main("books/frankenstein.txt")