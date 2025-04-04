from stats import *
import sys

def main():
    #path_to_file = "books/frankenstein.txt"
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book_file = sys.argv[1]
    book_text = get_book_text(path_to_book_file)
    character_counts_dict = get_num_characters(book_text)
    character_counts_list = convert_dict_to_list(character_counts_dict)
    character_counts_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_book_file} ---", end="\n\n")
    print(f"{get_num_words(book_text)} words found in the document", end="\n\n") 

    for c in character_counts_list:
        print(f"{c["name"]}: {c["num"]}")
        #print(f"The {c["name"]} character was found {c["num"]} times")

    print(f"\n--- End report of {path_to_book_file} ---")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read() 

def convert_dict_to_list(character_counts):
    character_counts = filtered_statistics_dict(character_counts)
    count_list = []
    for c in character_counts:
        count = character_counts[c]
        new_dict = {"name" : c[0], "num" : count}
        count_list.append(new_dict)
    return count_list

def sort_on(dict):
    return dict["num"]

main()