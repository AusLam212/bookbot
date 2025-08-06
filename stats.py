def count_words(text):
    words_list = text.split()
    word_count = len(words_list)
    print(f"Found {word_count} total words")

def count_characters(text):
    def sort_on(items):
        return items["num"]
    
    characters = {}

    lowercase_text = text.lower()

    for char in lowercase_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    characters_list = []

    for char in characters:
       if char.isalpha():
           if char is not characters_list:
                new_dict = {}

                new_dict["char"] = char
                new_dict["num"] = characters[char]

                characters_list.append(new_dict)

    characters_list.sort(reverse=True, key=sort_on)

    for char in characters_list:
        print(f"{char["char"]}: {char['num']}")