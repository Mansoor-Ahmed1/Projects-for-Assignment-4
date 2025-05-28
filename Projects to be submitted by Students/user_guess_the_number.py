import random

score = 10
num = random.randint(1,100)
print(num)
def main():
    global score
    while(score>0):
        user_guess = int(input(f"Guess a Number between 1 and 100!"))         
        if user_guess == num:
            print(f"""Congrats, You got that right!
                  You obtained {score} points out of 10.""")
            break
        elif user_guess > num:
            score -= 1  
            print(f"Your guessed number is Greater, {score} Attempts left.")
    
        elif user_guess < num:
            score -= 1
            print(f"Your guessed number is Lesser, {score} Attempts left.")
    else:
        print(f"Game over! You've used all your attempts. The number was {num}.")
        
if __name__ == "__main__":
    main()