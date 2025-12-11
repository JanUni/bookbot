def get_num_words(filepath):
    with open(filepath) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
        words_count = file_contents.split()
        return words_count

def get_letter_stats(filepath):
    word_dictionary = {}
    with open(filepath) as f:
        file_content = f.read()
        for letter in file_content:
            letter_lowercase = letter.lower()
            if letter_lowercase not in word_dictionary:
                word_dictionary[letter_lowercase] = 1
            else:
                word_dictionary[letter_lowercase] += 1
    return word_dictionary

def sort_on(items):
    return items["num"]

def return_sorted_list(word_dictionary):
    list = []
    for item in word_dictionary:
        new_dict_entry = {}
        new_dict_entry["char"] = item
        new_dict_entry["num"] = word_dictionary[item]
        list.append(new_dict_entry)
    list.sort(reverse=True, key=sort_on)
    return list
