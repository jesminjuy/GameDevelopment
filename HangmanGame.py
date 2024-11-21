import random

print("WELCOME TO HANGMAN GAME")

hangman = [
    r"""
        +---+
            |
            |
            |
           ===
    """,
    r"""
        +---+
        |   |
        0   |
            |
           ===
    """,
    r"""
        +---+
        |   |
        0   |
       /|   |
           ===
    """,
    r"""
        +---+
        |   |
        0   |
       /|\  |
           ===
    """,
    r"""
        +---+
        |   |
        0   |
       /|\  |
        |   ===
    """,
    r"""
        +---+
        |   |
        0   |
       /|\  |
        |   ===
       / \
    """
]

secret = ["tiger", "deer", "lion", "donkey"]
word = random.choice(secret).lower()
guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = 0

while tries > 0:
    output = ""
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += "-"

    print("\nGuess the word:", output)
    print(tries, "chances left")
    guess = input("Enter a letter: ").lower()

    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already guessed", guess)
    elif guess in word:
        print("GREAT! You have guessed a correct letter!")
        guessed_correctly.append(guess)
    else:
        print("SORRY! You have guessed a wrong letter!")
        tries -= 1
        print(hangman[hangman_count])
        hangman_count += 1
        guessed_incorrectly.append(guess)

    if output == word:
        print("\nCongratulations! You win!!")
        break
else:
    print("\nGAME OVER! You have lost. Try again.")
    print("The hidden word was:", word)

quit()