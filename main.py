def main():
    book_path = "books/frankenstein.txt"
    file_content = get_file_content(book_path)
    number_of_words = get_number_of_words(file_content)
    number_per_character = get_number_per_character(file_content)
    sorted_characters_by_num = sort_chars(number_per_character)
    print_report(book_path, number_of_words, sorted_characters_by_num)

def print_report(book_path, number_of_words, sorted_characters_by_num):
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words found in the document")
    print("")
    for element in sorted_characters_by_num:
        print(f"The '{element["letter"]}' character was found {element["num"]} times")
    print("--- End report ---")

def sort_chars(number_per_character):
    sorted_list = []
    for char in number_per_character:
        sorted_list.append({"letter" : char, "num" : number_per_character[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return(sorted_list)

def sort_on(dict):
    return dict["num"]

def should_skip(letter):
    not_supported_characters = ["#", ".", " ", "&", "@", "$", "%", "/", "_", "[", "]", "(", ")"]
    return letter in not_supported_characters

def get_number_per_character(text):
    result = {}
    for letter in text.lower():
        if should_skip(letter):
            continue
        try:
            result[letter] = result[letter] + 1
        except Exception as e:
            result[letter] = 1
    return result

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_file_content(book_path):
    with open(book_path) as f:
        return f.read()

main()
