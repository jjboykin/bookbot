def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    print(f"Word Count:{count_book_words(book_text)}")
    print(f"Character Counts:{count_book_characters(book_text)}")

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

main()