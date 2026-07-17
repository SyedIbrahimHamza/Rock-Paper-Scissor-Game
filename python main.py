
import random

choices = ["Rock", "Paper", "Scissors"]


user_score = 0
computer_score = 0

while True:  
    
    
    user_choice = input("\nEnter Your Choice (Rock, Paper, Scissors): ").title()
    
    
    if user_choice not in choices:
        print("Galat choice! Rock, Paper ya Scissors likho.")
        continue  
    
    computer_choice = random.choice(choices)
    print(f"Computer's Choice: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a Tie!")
    
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
        user_score += 1  
    
    else:
        print("You lose!")
        computer_score += 1  
    
    print(f"Score -> Aap: {user_score} | Computer: {computer_score}")
    
    
    play_again = input("\nAur khelna hai? (yes/no): ").lower()
    if play_again != "yes":
        print("\nGame Khatam! 🎮")
        print(f"Final Score -> Aap: {user_score} | Computer: {computer_score}")
        break  

