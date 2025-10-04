import sys
from stats import get_num_words, count_occurances, sort_dict, sort_on 
def get_book_text(file):
    with open(file) as f:
        return f.read()
def main():
    try:
        arg1 = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        #exit()
    book = arg1
    looking = get_book_text(arg1)
    print(f"Found {get_num_words(looking)} total words")
    looking = count_occurances(looking)
    x = sort_dict(looking)
    #print(x)
    for i in x:
        print(f"{i["char"]}: {i["num"]}")

main()
