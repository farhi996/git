import random
print("Välkommen")
name = input("Ange ditt namn? ") 
print("Lycka till! ", name) 
words = ['flyga','ensam','vaken','kramp','bonus','boxer',]
print("Du har 5 försök att gissa ordet korrekt.")
word = random.choice(words) 
print("Gissa ordet") 
guesses = ''
turns = 5

while turns > 0:


    failed = 0

    for char in word:

        if char in guesses:  
            print(char) 


        else:  
            print("_") 
              
           
            failed += 1

    if failed == 0: 
        print("Grattis du vann!")
        print("Du vann med", + turns,'gissningar') 

        print("Ordet är: ", word)  
        break

    guess = input("Gissa ordet:") 

    guesses += guess  
    if guess not in word: 
         turns -= 1
         print("OBS Fel Svar") 
         print("Du har", + turns, 'fler gissningar') 
         if turns == 0: 
            print("Du förlorar") 
            print("Ordet är: ", word)

# Feedback uppskattas
