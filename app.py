# write 'hello world' to the console
import random

def get_computer_choice():
	return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
	valid_choices = ['rock', 'paper', 'scissors']
	while True:
		choice = input("Choose rock, paper, or scissors: ").strip().lower()
		if choice in valid_choices:
			return choice
		print("Invalid option. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(player, computer):
	if player == computer:
		return 'tie'
	if (
		(player == 'rock' and computer == 'scissors') or
		(player == 'scissors' and computer == 'paper') or
		(player == 'paper' and computer == 'rock')
	):
		return 'win'
	return 'lose'

def play_game():
	score = 0
	rounds = 0
	while True:
		print("\n--- New Round ---")
		player = get_player_choice()
		computer = get_computer_choice()
		print(f"You chose: {player}")
		print(f"Computer chose: {computer}")
		result = determine_winner(player, computer)
		if result == 'win':
			print("You win this round!")
			score += 1
		elif result == 'lose':
			print("You lose this round.")
		else:
			print("It's a tie.")
		rounds += 1
		again = input("Play again? (y/n): ").strip().lower()
		if again != 'y':
			break
	print(f"\nGame over! You played {rounds} round(s). Your score: {score}")

if __name__ == "__main__":
	play_game()
print('hello world')