import random
# lets start with some pseudocode and TDD

def main():
    compare_weapons()
    play_round()


def play_round():
    for i in range(5):
        if i == 0:
            i = i + 1
            compare_weapons()
        print(i)


def play_game():
    ...


def compare_weapons():
    weapon_list = ["Rock", "Paper", "Scissors"]
    program_weapon = random.choice(weapon_list)
    print(program_weapon)
    player_weapon = input("Choose your weapon!\n").title()
    if player_weapon == "Rock" or player_weapon == "Paper" or player_weapon == "Scissors":
        print(f"You chose: {player_weapon}")
    else:
        print("Not a valid weapon")
    if player_weapon == program_weapon:
        print("It's a draw!")
    else:
        print("Let's try and get a draw next time")


if __name__ == "__main__":
    main()


# required functionality:
# give user chance to pick weapon either in args or from options
# get the program to randomly choose a weapon
# compare the weapons
# announce the winner of that round
# play 5 rounds and announce overall winner