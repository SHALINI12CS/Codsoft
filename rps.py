import random

def get_computer_choice():
    # Generate a random choice for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on game logic
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        # Prompt the user for their choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        # Generate the computer's choice
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and display the result
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display scores
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

# Run the main function
if __name__ == "__main__":
    main()
