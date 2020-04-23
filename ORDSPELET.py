import random  # för att kunna använda dig av random.choice senare


def reading_file():  # en funktion som läser orden från dokumentet "word.txt" och sedan omvandlar alla ord till en lista
    # öppnar filen och läser bara
    f = open("word.txt", "r")
    empty_list = []  # vi gör en tom lista som vi senare kan lägga ord i
    for line in f:  # för varje rad i dokumentet
        stripped_line = line.strip()  # separerar orden i textfilen
        # sätter alla orden i en lista separerade
        empty_list.append(stripped_line)

    return empty_list  # returnererar listan


def generate_word():  # en funktion som genererar ett slumpmässigt ord från textfilen
    # tillsätter returvärdet från reading_file() (listan med ord) till variabeln words
    words = reading_file()
    # genererar ett slumpmässigt ord från listan och tillsätter ordet i variabeln word
    word = random.choice(words)
    return word  # returnerar ordet


def welcome_screen():  # en välkomstskärm
    print("Välkommen") 
    name = input("Ange ditt namn? ")
    print("Lycka till! ", name)
    print("Du har 5 försök att gissa ordet korrekt.")
    print("OBS! 5 bokstäver, inte mer eller mindre")


def main():
    welcome_screen()
    # tillsätter variabeln actual_word ett slumpmässigt valt ord
    actual_word = generate_word()
    guesses = ''
    turns = 5  # max 5 antal gissningar
    while turns > 0:  # tills antal gissningar har nått 5 ska programmet köras
        failed = 0 # räknar ut hur många gånger användares fejlar
        guess = input("Gissa ordet:")
        if len(guess) != 5:  # om längden av gissningen inte är 5...
            print("Endast 5 bokstäver tillåtna")
        else:  # rätt antal bokstäver har lagts in
            guesses += guess  # en gissning gjord
            if guess not in actual_word:  # om någon bokstav i gissningen inte finns i ordet...
                turns -= 1  # minskar turns om man inte har gissat rätt ord...
                print("OBS! Fel Svar")
                print("Du har", + turns, 'fler gissningar')
                if turns == 0:  # spelet är slut då användaren inte har några gissningar kvar
                    print("Du förlorar")
                    print("Ordet är: ", actual_word)
            for char in actual_word:  # för varje bokstav i givna ordet, om bokstaven finns i din gissning så ska den printas
                if char in guesses:
                    print(char)
                else:  # annars skriv ut understreck
                    print("_")
                    failed += 1
            if failed == 0:  # användaren vinner om failed == 0
                print("Grattis du vann!")
                print("Du vann med", + turns, 'gissningar kvar')
                print("Ordet är: ", actual_word)
                break


main()
