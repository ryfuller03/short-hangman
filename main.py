# following these rules: https://codegolf.meta.stackexchange.com/a/11925
import random
def main():
    print("Welcome to Hangman!\nHere are the rules:\nYou must complete the random word letter by letter\nbefore the man is fully built.\nEach incorrect guess creates a limb out of thin air.\nGood luck!")
    word, guesses, total_guesses, lost, user_letters, hangman = [i for i in random.choice([i.strip() for i in (open("randomwords.txt", 'r')).readlines()])], 6, 0, False, set(), "---------------\n|              \n|             \n|             "

    # 1 more line, but much fewer chars for line 5
    letters = ["_" for _ in word]
    while "".join(letters)!=word and not lost:
        print(f"Here is your current hangman:\n{hangman}\n{' '.join(letters)}\nYou have {guesses} guesses left.\nHere are your guessed letters: {', '.join(user_letters)}");get_letter = input("Please guess a letter: ")
        if get_letter in word:
            for i in range(len(word)):
                if word[i]==get_letter:letters[i]=get_letter
            user_letters.add(get_letter);total_guesses+=1;print("Great! You got it!")
        else:print("That letter is not in the word. Please try again. :(");hangman = update_hangman(hangman, guesses);user_letters.add(get_letter);total_guesses+=1;guesses-=1;
        if guesses == 0:lost = True
    print(f"{hangman}\nYou lose! The word was {word}. Nice try!") if lost else print(f"Congratulations! You got it within {total_guesses} guesses!")
def update_hangman(hangman: str, remaining: int) -> str:
    hgmn=hangman.split('\n')
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
main()
# [(1, 'O'), (2, '/')] <- for shortening the match statements