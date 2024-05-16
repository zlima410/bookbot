if __name__ == "__main__":
    def get_num_words(text):
        words = text.split()
        return len(words)

    def get_char_dict(text):
        chars = {}
        for c in text:
            if c.isalpha():
                lowered = c.lower()
                if lowered in chars:
                    chars[lowered] += 1
                else:
                    chars[lowered] = 1
        return chars
    
    def sort_dict(d):
        sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        for item in sorted_dict.items():
            print(f"The '{item[0]}' character was found {item[1]} times")
        return ""

    def get_book_text(path):
        with open(path) as f:
            return f.read()
        
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_dict = get_char_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print(f"{sort_dict(letter_dict)}")
    print(f"--- End report ---")