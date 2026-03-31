# Homework 3 - Board Game System
# Name: Miguel Alvarado
# Date: 3/30/2026

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)


def movePlayer(data):
    """Moves the current player in the game and updates the game"""

    CurrentPlayer = data[0].split(": ")[1]
    CurrentIndex = -1
    CurrentPosition = 0

    for i in range(1, len(data)):
        line = data[i]
        parts = line.split(": ")

        name = parts[1]
        position = parts[0]

        if name == CurrentPlayer:
            CurrentIndex = i
            CurrentPosition = int(position)
    move = int(input("How many spaces to move? "))
    NewPosition = CurrentPosition + move

    if NewPosition >= 30:
        print(CurrentPlayer + " wins the game!")
        return

    NewLine = str(NewPosition) + ": " + CurrentPlayer

    data[CurrentIndex] = NewLine
    print(CurrentPlayer + " moved to space " + str(NewPosition))

    for i in range(1, len(data)):
        parts = data[i].split(": ")

        position = int(parts[0])
        name = parts[1]

        if position == NewPosition:
            if name != CurrentPlayer:
                if name == "Treasure":
                    print(CurrentPlayer + " You found Treasure!")
                elif name == "Trap":
                    print(CurrentPlayer + " Aww man you landed on a trap!")
                elif name == "Heal":
                    print(CurrentPlayer + " Nice! you healed up!")
                elif "Player" in name:
                    print(CurrentPlayer + " landed on " + name)

   #This switches turns 
    if CurrentPlayer == "Player1":
        nextPlayer = "Player2"
    elif CurrentPlayer == "Player2":
        nextPlayer = "Player 3"
    else:
        nextPlayer = "Player1"
    
    data[0] = "Turn: " + nextPlayer


def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    
    while True:
        displayGame(gameData)

    # Example interaction
        choice = input("\nMove player? (y/n): ")
        if choice.lower() != "y":
            print("Game over!")
            break
        movePlayer(gameData)
        print()


if __name__ == "__main__":
    main()
