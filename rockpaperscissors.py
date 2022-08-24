import random
def get_choices(): #creates a function to get choices
     player_choice = input("Enter a choice(rock, paper, or scissors): ") #take in users choice
     options = ["rock", "paper", "scissors"] #list to declare options for the computer
     computer_choice = random.choice(options) #randomly selects an option for the computer
     choices = {"player": player_choice, "computer": computer_choice} #dict to store choices of player and computer

     return choices #calls the function


def check_win(player, computer): 
     print(f"You chose {player}, computer chose {computer}.") #fstring makes concatenation easier/prints out choices made
     if player == computer: 
        return "It's a tie!"
     elif player == "rock":
        if computer == "paper": 
            return "Paper covers rock! You lose." 
        else:
            return "Rock beats scissors! You win!" 
     elif player == "paper":
        if computer == "scissors": 
            return "Scissors cut paper! You lose."
        else:
            return "Paper covers rock! You win!"
     elif player == "scissors":
        if computer == "rock": 
            return "Rock beats scissors! You lose!"
        else:
            return "Scissors cut paper! You win!"
    
choices = get_choices() #gets choices
result = check_win(choices["player"], choices["computer"]) #calls the check_win function and passes in choices picked from dictionary above
print(result)