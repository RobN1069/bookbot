def main():
    path_to_file = "books/frankenstein.txt"
    document_text = get_document_text(path_to_file)
    word_count = get_num_words(document_text)
    character_dict = get_chars_dict(document_text)
    sorted_list = chars_dict_to_sorted_list(character_dict)

    print(f"---- Begin report of {path_to_file} ----")
    print(f"{word_count} found in this document")
    print()

    for letter in sorted_list:
        if not letter["char"].isalpha():
            continue
        print(f"The '{letter['char']}' character was found {letter['num']} times")
    print("---- End of report ----")


def get_num_words(text):
    words = text.split()
    return(len(words))


def sort_on(sort_column):
    return sort_column["num"]


def chars_dict_to_sorted_list(dict_to_sort):
    sorted_list = []
    for ch in dict_to_sort:
        sorted_list.append({"char": ch, "num": dict_to_sort[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    text = text.lower()
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def get_document_text(path):
    with open(path) as f:
        return f.read()


main()
