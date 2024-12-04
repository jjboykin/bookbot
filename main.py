def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    character_counts_dict = count_book_characters(book_text)
    character_counts_list = convert_dict_to_list(character_counts_dict)
    character_counts_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_file} ---", end="\n\n")
    print(f"{count_book_words(book_text)} words found in the document", end="\n\n") 

    for c in character_counts_list:
        print(f"The {c["name"]} character was found {c["num"]} times")

    print(f"\n--- End report of {path_to_file} ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read() 

def count_book_words(book_text):
    return len(book_text.split())

def count_book_characters(book_text):
    char_counts = {}
    for c in book_text.lower():
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

def convert_dict_to_list(character_counts):
    character_counts = filtered_statistics_dict(character_counts)
    count_list = []
    for c in character_counts:
        count = character_counts[c]
        new_dict = {"name" : c[0], "num" : count}
        count_list.append(new_dict)
    return count_list

def filtered_statistics_dict(character_count_dict):
    filtered = {}
    for c in character_count_dict:
        count = character_count_dict[c]
        #print(f"{c}:{count}")
        if c.isalpha():
            filtered[c[0]] = count
    return filtered

def sort_on(dict):
    return dict["num"]

main()