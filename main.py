from stats import get_num_words, get_letter_stats, return_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    words_count = get_num_words(book_path)
    letter_count_dictionary = get_letter_stats(book_path)
    sorted_list = return_sorted_list(letter_count_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(words_count)} total words")
    print("--------- Character Count -------")
    for letter in sorted_list:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

main()