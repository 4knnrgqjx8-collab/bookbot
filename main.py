import sys
from stats import number_words, characters, sortifying 
def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_words(sys.argv[1])} total words")
    a = sortifying(characters(sys.argv[1]))
    print("--------- Character Count -------")
    for i in a:
        if i["character"].isalpha() == True:
            print(f'{i["character"]}: {i["count"]}')
    print("============= END ===============")
if sys.argv == ["main.py"]:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    main()
