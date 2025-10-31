import random


def main():
    file = open("./combined_wordlist.txt", "r")
    words = file.read()
    
    word_list = words.split("\n")

    winner_word = random.choice(word_list)

    print(winner_word)

if __name__ == "__main__":
    main()