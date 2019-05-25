sample_word = "test"
limit = 5
guess = ""
guesses = 0
win = False
print("Haslo ma", len(sample_word), "litery")
print("Posiadasz", limit, "prob.")

while guesses != limit:
    print("Pozostalo ci", limit - guesses, "prob.")
    guess = input("Podaj litere: ")

    if guess == sample_word:
        win = True
        break
    elif guess in sample_word:
        print("Litera jest w slowie na pozycji:", sample_word.find(guess) + 1)
    else:
        print("Zle!")

    guesses += 1

if win == True:
    print("Wygrales! Slowo to:", sample_word)
else:
    print("Przegrales!")