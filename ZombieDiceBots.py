print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
import random

class Gamer:
    def __init__(self, player_name):
        self.player_name = player_name
        self.total_score = 0

    def roll_dice(self):
        return [random.choice(['brain', 'shotgun', 'footprint']) for _ in range(3)]

def start_game():
    first_player_name = input("Enter the name of Player 1: ")
    second_player_name = input("Enter the name of Player 2: ")
    first_player = Gamer(first_player_name)
    second_player = Gamer(second_player_name)

    while True:
        for current_player in [first_player, second_player]:
            print(f"{current_player.player_name}'s turn")
            input("Press Enter to roll the dice...")
            dice_rolls = current_player.roll_dice()
            print(f"Rolled: {dice_rolls}")
            brain_count = dice_rolls.count('brain')
            shotgun_count = dice_rolls.count('shotgun')
            current_player.total_score += brain_count
            print(f"{current_player.player_name} scored {brain_count} brains. Total score: {current_player.total_score}")

            if shotgun_count > 0:
                print(f"{current_player.player_name} got shotguns! Turn over.")
                break

        if current_player.total_score >= 13:
            print(f"{current_player.player_name} wins with a score of {current_player.total_score}!")
            break

start_game()
