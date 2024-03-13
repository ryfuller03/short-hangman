# following these rules: https://codegolf.meta.stackexchange.com/a/11925
import random


def instructions():
    print("Welcome to Hangman!\nHere are the rules:\n"
          "You must complete the random word letter by letter\nbefore the man is fully built.\n"
          "Each incorrect guess creates a limb out of thin air.\n"
          "Good luck!")


def main():
    instructions()
    word = [i for i in random.choice([i.strip() for i in (open("randomwords.txt", 'r')).readlines()])]
    guesses = 6
    total_guesses = 0
    lost = False
    user_letters = set()
    hangman = "---------------\n|              \n|             \n|             "
    letters = ["_"for _ in word]
    while letters != word and not lost:
        print("".join(word))
        print(f"Here is your current hangman:\n{hangman}\n")
        print(" ".join(letters))
        print(f"You have {guesses} guesses left.")
        if len(user_letters) != 0:
            print(f"Here are your guessed letters: {', '.join(user_letters)}")
        get_letter = input("Please guess a letter: ")
        if get_letter in word:
            letters[word.index(get_letter)] = get_letter
            user_letters.add(get_letter)
            total_guesses += 1
            print("Great! You got it!")
        else:
            print("That letter is not in the word. Please try again. :(")
            hangman = update_hangman(hangman, guesses)
            user_letters.add(get_letter)
            total_guesses += 1
            guesses -= 1
            if guesses == 0:
                lost = True
    if lost:
        print(f"{hangman}")
        print("Aw man, nice try!")
    else:
        print(f"Congratulations! You got it within {total_guesses} guesses!")


def update_hangman(hangman: str, remaining: int) -> str:
    hgmn = hangman.split('\n')
    match remaining:
        case 6:
            hgmn[1] += "0"
        case 5:
            hgmn[2] += "/"
        case 4:
            hgmn[2] += "|"
        case 3:
            hgmn[2] += '\\'
        case 2:
            hgmn[3] += "/"
        case 1:
            hgmn[3] += " \\"

    return "\n".join(hgmn)


#  used for getting our randomwords.txt file (didn't want weird nonsense words or super long ones in there)
# def random_words_list():
#     file = open("english3.txt", 'r')
#     words = []
#     for word in file.readlines():
#         if (len(word) < 7) and (len(word) > 4):
#             words.append(word)
#     f = open("randomwords.txt", 'w')
#     f.write(''.join(words))
#     f.close()


main()
