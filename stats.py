def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    char_counts = {}
    for c in book_text.lower():
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

def filtered_statistics_dict(character_count_dict):
    filtered = {}
    for c in character_count_dict:
        count = character_count_dict[c]
        #print(f"{c}:{count}")
        if c.isalpha():
            filtered[c[0]] = count
    return filtered