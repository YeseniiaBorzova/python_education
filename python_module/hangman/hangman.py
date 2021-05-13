"""Module that contains Hangman class that imitates Hangman game"""
import random


class Hangman:
    """Game representing class"""
    word_list = ["cat", "mathematics", "wombat", "insect", "honda", "civic", "dictionary"
                 "tree", "astronaut", "lamp", "dragon", "python", "table", "sunflower"]
    stages = ['''
+---+
     |
     |
     |
    ===''', '''
+---+
 O   |
     |
     |
    ===''', '''
+---+
 O   |
 |   |
     |
    ===''', '''
+---+
 O   |
/|   |
     |
    ===''', '''
+---+
 O   |
/|\  |
     |
    ===''', '''
+---+
 O   |
/|\  |
/    |
    ===''', '''
+---+
 O   |
/|\  |
/ \  |
    ===''']

    def take_random_word(self) -> str:
        """:return randomly selected word from list of available words"""
        word = random.choice(self.word_list)
        return word.upper()

    def display_state_of_hangman(self, tries) -> str:
        """:return state of hangman according to the amounts of tries left"""
        return self.stages[tries]

    def play(self):
        """Main method responsible for the whole game process.
        It is responsible for guessing the word and displaying
        information about guessed letters"""
        word = self.take_random_word()
        word_completion = "_" * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6
        print("Let's play Hangman")
        print(self.display_state_of_hangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            guess = input("guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("you already tried", guess, "!")
                elif guess not in word:
                    print(guess, "isn't in the word :(")
                    tries -= 1
                    guessed_letters.append(guess)
                else:
                    print("Nice one,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already tried ", guess, "!")
                elif guess != word:
                    print(guess, " isn`t that word! :(")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("invalid input")
            print(self.display_state_of_hangman(tries))
            print(word_completion)
            print("\n")
        if guessed:
            print("Good Job, you guessed the word!")
        else:
            print("I'm sorry, but your tries ran out. The word was " + word + ". Maybe next time!")


def main():
    """function that creates Hangman game object and starts gaming loop"""
    hangman = Hangman()
    hangman.play()
    while input("Again? (Y/N) ").upper() == "Y":
        hangman.play()


if __name__ == "__main__":
    main()
