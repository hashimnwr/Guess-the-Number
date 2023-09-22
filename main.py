import random

end_game = False
NUMBER = random.randint(1, 100)
print("Welcome to number guessing game...\nI'm thinking a number between 1 and 100.")
difficulty = input("Choose difficulty level, 'easy' or 'hard' : ").lower()

if difficulty == 'hard':
    lives = 5
elif difficulty == 'easy':
    lives = 10
else:
    print("input error, please check the spelling...")
    end_game = True
  
while not end_game:
    guess = input("Make a guess: ")
    guess = int(guess)
    diff = abs(guess - NUMBER)
    if guess == NUMBER:
        print(f"You guessed it right, with {lives} lives remaining...")
        end_game = True
    else:
        lives -=1
        print(f'You have {lives} attempts left')
        if lives == 0:
            end_game = True
            print(f"Answer = {NUMBER}")
        else:
            if guess > NUMBER:
                print("High")
                if diff < 3:
                    print("too close")
            elif guess < NUMBER:
                print("Low")
                if diff < 3:
                    print("too close")
