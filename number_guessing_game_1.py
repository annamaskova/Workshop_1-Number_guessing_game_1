from random import randint

# font rectangles
print("""
                                                                                                
 _____           _              _____                 _            _____                  ___   
|   | |_ _ _____| |_ ___ ___   |   __|_ _ ___ ___ ___|_|___ ___   |   __|___ _____ ___   |_  |  
| | | | | |     | . | -_|  _|  |  |  | | | -_|_ -|_ -| |   | . |  |  |  | .'|     | -_|   _| |_ 
|_|___|___|_|_|_|___|___|_|    |_____|___|___|___|___|_|_|_|_  |  |_____|__,|_|_|_|___|  |_____|
                                                           |___|                                
                 --------Guess the natural number from 1 to 100--------    
                                                       """)

game_is_on = True
drawn_num = randint(1, 100)

while game_is_on:
    try:
        guess_num = int(input("Guess the number: "))
    except ValueError:
        print("It's not a natural number!")
        continue
    if guess_num < drawn_num:
        print("Too small!")
    elif guess_num > drawn_num:
        print("Too big!")
    else:
        print("You win!")
        game_is_on = False
