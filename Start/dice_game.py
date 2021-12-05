import random

def dice():
    return random.randint(1,6) + random.randint(1,6)

def main():
    player1 = input("Enter Player 1's name:")
    player2 = input("Enter Player 2's name:")

    roll1 = dice()
    roll2 = dice()

    print(player1,"rolled",roll1)
    print(player2,"rolled",roll2)

    if roll1 > roll2:
        print(player1,"wins!")
    elif roll1 < roll2:
        print(player2,"wins!")
    else:
        print("You tie!")
main()