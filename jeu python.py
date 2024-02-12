import string  # the string module is imported to use ascii constants such as string.ascii_uppercase
import random


# Displays the game grid with row and column coordinates (def print_grid)
def print_grid(grid):
    # Displays the game board with the column coordinates (A, B, C, D, E)
    print("  " + "  ".join(f"{c:2}" for c in string.ascii_uppercase[:5]))
    # Scroll through the grid lines to display the symbols and separate the lines with horizontal lines
    for i, line in enumerate(grid):
        # Displays line numbers and line symbols separated by vertical bars
        print(str(i + 1) + " " + " | ".join(line))

        # Displays a horizontal line between each line except the last
        if i < 4:
            print(" " + "-" * 19)  # Separation line between the lines on the board


# Check whether a player has won by examining the rows, columns and diagonals (def validate_win)
def validate_win(grid, symbol):
    # Check rows, columns, and diagonals for the specified symbol (X or O)
    for i in range(5):
        # Check rows
        if all(grid[i][j] == symbol for j in range(5)):
            return True

        # Check columns
        if all(grid[j][i] == symbol for j in range(5)):
            return True

    # Check diagonals
    if all(grid[i][i] == symbol for i in range(5)) or all(
        grid[i][4 - i] == symbol for i in range(5)
    ):
        return True

    return False


def choice_position(enter):
    # Converts an alphanumeric position (for example: C2) into grid coordinates (row, column)
    if (
        len(enter) != 2
        or enter[0].upper()
        not in string.ascii_uppercase[
            :5
        ]  # Checks whether the first character is a letter between A and E
        or not enter[1].isdigit()  # Checks whether the second character is a number
    ):
        raise ValueError("Enter invalid. Please enter a valid position (e.g. A3)")

    column = string.ascii_uppercase.index(
        enter[0].upper()
    )  # Converts the letter to a column index
    line = int(enter[1]) - 1  # Converts the number to a line index

    if line not in range(5):  # Checks whether the line index is valid (between 0 and 4)
        raise ValueError("Enter invalid. Please enter another valid position")
    return line, column  # Returns grid coordinates (row, column)


# Generates a valid random movement for the AI
def random_stroke(grid):
    # A random move valid for the AI and lists of the coordinates of the empty squares
    random_stroke = [(i, j) for i in range(5) for j in range(5) if grid[i][j] == " "]
    if random_stroke:  # if there are empty boxes in the grid
        choice = random.choice(random_stroke)
        column = choice[1]  # for columns
        row = choice[0]  # for rows
        return column, row
    else:
        return None  # no empty boxes


def choice_symbol():
    while True:
        # Asks the player to choose a symbol (X or O) and converts the input to capitals
        symbol = input("Choose your symbol X or O: ").upper()
        if symbol in ["X", "O"]:  # Checks whether the chosen symbol is valid (X or O)
            return symbol  # Returns the chosen symbol if it is a valid choice
        else:
            print("Invalid symbol. Please choose between X and O.")
            # Displays an error message if the symbol chosen is invalid


def morpion():
    print("Hello! Welcome to Morpion!")  # Welcome message

    player_symbol = choice_symbol()  # Choosing player symbol
    ai_symbol = (
        "O" if player_symbol == "X" else "X"
    )  # Assigning AI symbol based on player's choice
    print(f"You have chosen the symbol. You will play against the ai with the symbol.")

    while True:
        grid = [
            [" " for _ in range(5)] for _ in range(5)
        ]  # Initialize an empty grid for the game
        symbols = [player_symbol, ai_symbol]
        tour = 0  # Initialize the turn counter

        while True:
            print_grid(grid)  # Displaying the current grid
            player = symbols[
                tour % 2
            ]  # Obtaining the symbol for the current player based on the turn number

            if player == player_symbol:  # Player's turn
                while True:
                    try:
                        answer = input(
                            f"Player {player_symbol}, enter your move (e.g. A1): "
                        )
                        line, column = choice_position(answer)
                        if grid[line][column] == " ":  # Checks if the box is empty
                            grid[line][
                                column
                            ] = player  # Place the player's symbol in the square
                            break
                        else:
                            print(
                                "This box is already occupied. Choose another box."
                            )  # Indicates that the box is already occupied
                    except ValueError:
                        print(
                            "Invalid input. Please enter a valid position"
                        )  # Management of an invalid entry

            else:  # AI's turn
                column, line = random_stroke(grid)
                print(
                    f"The AI chose position {string.ascii_uppercase[column]}{line + 1}."
                )  # Display of the position chosen by the ai
                grid[line][column] = player

            # Check if there is a winner fot both the player and the AI
            if validate_win(grid, player_symbol) or validate_win(grid, ai_symbol):
                print_grid(grid)
                if player == player_symbol:
                    print("Congratulations you win!")
                else:
                    print("The AI wins!")
                break  # Exit the game loop when a winner is found

            # Check if it's a draw
            if tour == 24:
                print_grid(grid)
                print("Draw!")
                break

            tour += 1  # Increments the turn counter to move on to the next turn (next player or AI)

        play_again = input(
            "Do you want to play again? yes/no: "
        )  # Asks the user if they want to play again
        if (
            play_again.lower() != "yes"
        ):  # Checks if the user response is not "yes" (case insensitive)
            print("Thank you for playing, goodbye!")
            break


if __name__ == "__main__":
    morpion()
