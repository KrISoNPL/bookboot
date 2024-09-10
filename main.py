def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_words_count(text)
    character_count = get_character_count(text)
    print(f"--- Book path: {book_path} ---")
    print(f" ")
    print(f"Word Count: {word_count}")
    print(f" ")
    print(f"Character Count:")
    for character, count in character_count.items():
       print(f'"{character}" = {count} ') 
    print(f" ")
    print(f"---END---")

def get_book_text(path):
    with open(path) as f:
       return f.read()
    
def get_words_count(text):
    words = text.split()
    count = len(words)
    return count

def get_character_count(text):

    lowered_text = text.lower()
    words = lowered_text.split()
    character_dict = {}

    for word in words:

        #print(word)
        characters = list(word)
        #print(characters)

        for character in characters:
            if(character in character_dict):
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        
    return character_dict

    

main()

