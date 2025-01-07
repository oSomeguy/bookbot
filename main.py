def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    num_letters = get_letter_count(text)
#    print(text)
    print(f"{word_count} words found in this document.")
    for letter, count in num_letters.items():
        print(f"The letter {letter.capitalize()} occured {count} times.")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letter_count = {     
    }
    lower = text.lower()
    for letter in letters:
        letter_count[letter] = lower.count(letter)
    return letter_count

main()