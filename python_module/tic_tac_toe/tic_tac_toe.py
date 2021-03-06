import os
import logging
from datetime import datetime


class Board:
    first_player = None
    second_player = None

    def __init__(self):
        self.first_player_choice = " "
        self.second_player_choice = " "
        self.first_player_score = 0
        self.second_player_score = 0
        self.cells = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]

    def display(self):
        print(" %s | %s | %s " % (self.cells[0][0], self.cells[0][1], self.cells[0][2]))
        print(" --------- ")
        print(" %s | %s | %s " % (self.cells[1][0], self.cells[1][1], self.cells[1][2]))
        print(" ---------")
        print(" %s | %s | %s " % (self.cells[2][0], self.cells[2][1], self.cells[2][2]))

    @staticmethod
    def welcome_user():
        print("Welcome to tic tac toe game!")

    def refresh_screen(self):
        os.system('clear')
        self.welcome_user()
        self.display()

    def get_board(self):
        return self.cells

    def get_amount_of_free_cells(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == " ":
                    count += 1
        return count

    def set_first_player_username(self, username):
        self.first_player = username

    def set_second_player_username(self, username):
        self.second_player = username

    def set_first_player_choice(self, choice):
        self.first_player_choice = choice.upper()

    def set_second_player_choice(self, choice):
        self.second_player_choice = choice.upper()

    def get_first_layer_username(self):
        return self.first_player

    def get_second_player_username(self):
        return self.second_player

    def get_first_layer_choice(self):
        return self.first_player_choice

    def get_second_layer_choice(self):
        return self.second_player_choice

    def update_first_player_score(self):
        self.first_player_score += 1

    def update_second_player_score(self):
        self.second_player_score += 1

    def update_score(self, player):
        if self.first_player_choice == player.upper():
            self.update_first_player_score()
        else:
            self.update_second_player_score()

    def get_first_layer_score(self):
        return self.first_player_score

    def get_second_player_score(self):
        return self.second_player_score

    def identify_player(self, player):
        if self.first_player_choice == player.upper():
            return self.first_player
        return self.second_player

    def update_cell(self, cell_coordinates, player):
        if player != "X" and player != "O":
            raise ValueError("You can only play with X or O")
        if self.cells[cell_coordinates[0] - 1][cell_coordinates[1] - 1] == " ":
            self.cells[cell_coordinates[0] - 1][cell_coordinates[1] - 1] = player

    @staticmethod
    def clear_logs():
        file = open('win_log.txt', "w")
        file.close()

    def is_winner(self, player):
        if self.cells[0][0] == player and self.cells[1][1] == player and self.cells[2][2] == player:
            self.update_score(player)
            return True
        elif self.cells[0][2] == player and self.cells[1][1] == player and self.cells[2][0] == player:
            self.update_score(player)
            return True
        elif self.cells[0][0] == player and self.cells[0][1] == player and self.cells[0][2] == player:
            self.update_score(player)
            return True
        elif self.cells[1][0] == player and self.cells[1][1] == player and self.cells[1][2] == player:
            self.update_score(player)
            return True
        elif self.cells[2][0] == player and self.cells[2][1] == player and self.cells[2][2] == player:
            self.update_score(player)
            return True
        elif self.cells[0][0] == player and self.cells[1][0] == player and self.cells[2][0] == player:
            self.update_score(player)
            return True
        elif self.cells[0][1] == player and self.cells[1][1] == player and self.cells[2][1] == player:
            self.update_score(player)
            return True
        elif self.cells[0][2] == player and self.cells[1][2] == player and self.cells[2][2] == player:
            self.update_score(player)
            return True
        else:
            return False

    def is_draw(self):
        used_cells = 0
        for cell_row in self.cells:
            for cell in cell_row:
                if cell != " ":
                    used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset_field(self):
        for i in range(3):
            for j in range(3):
                self.cells[i][j] = " "

    def minimax(self, cells, depth, is_max):
        if self.is_winner("O"):
            return 10
        elif self.is_winner("X"):
            return -10
        elif self.is_draw():
            return 0

        if is_max:
            max_score = -1000
            for i in range(len(cells)):
                for j in range(len(cells[i])):
                    if cells[i][j] == " ":
                        cells[i][j] = "O"
                        max_score = max(max_score, self.minimax(cells, depth + 1, not is_max))
                        cells[i][j] = " "
            return max_score
        else:
            max_score = 1000
            for i in range(len(cells)):
                for j in range(len(cells[i])):
                    if cells[i][j] == " ":
                        cells[i][j] = "X"
                        max_score = min(max_score, self.minimax(cells, depth + 1, not is_max))
                        cells[i][j] = " "
            return max_score

    def find_best_move(self, cells):
        best_val = -1000
        best_move = (-1, -1)

        for i in range(len(cells)):
            for j in range(len(cells[i])):
                if cells[i][j] == " ":
                    cells[i][j] = "O"
                    move_val = self.minimax(cells, 0, False)
                    cells[i][j] = " "
                    if move_val > best_val:
                        best_move = (i+1, j+1)
                        best_val = move_val

        print("The value of the best Move is :", best_move)
        return best_move

    def play(self):
        play_choice = input("Do you want to play vs AI? Y/N \n").upper()
        if play_choice == "N":
            username = input("Enter username for first player \n")
            self.set_first_player_username(username)
            choice = input(f"{username}, you want to play as X or O \n").upper()

            if choice == "X":
                self.set_first_player_choice("X")
                self.set_second_player_choice("O")
            elif choice == "O":
                self.set_first_player_choice("O")
                self.set_second_player_choice("X")
            else:
                print("Incorrect input")

            username = input("Enter username for second player \n")
            self.set_second_player_username(username)

            while True:
                self.refresh_screen()
                try:
                    x_choice = tuple(map(int, input("Enter coordinates, where you want to put X \n").split(',')))
                    self.update_cell(x_choice, "X")
                except (ValueError, IndexError):
                    print("Incorrect output!! Coordinates should be inputted in form '1,2'")
                self.refresh_screen()

                if self.is_winner("X"):
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    logging.basicConfig(filename='win_log.txt', filemode='a', level=logging.INFO)
                    logging.info(f"Winner:{self.identify_player('X')}, time:{now}")
                    print(f"{self.identify_player('X')}, X wins\n")
                    play_again = input("Want to play again Y/N? \n").upper()
                    if play_again == "Y":
                        self.reset_field()
                        continue
                    else:
                        print(f"Final score \nfirst player {self.first_player}:{str(self.first_player_score)} \n"
                              f"second player {self.second_player}:{str(self.second_player_score)}")
                        clean_logs = input("Do you want to clean logs? Y/N \n").upper()
                        if clean_logs == "Y":
                            self.clear_logs()
                        break

                if self.is_draw():
                    print("Its a draw!!!\n")
                    play_again = input("Want to play again Y/N? \n").upper()
                    if play_again == "Y":
                        self.reset_field()
                        continue
                    else:
                        print(f"Final score {self.first_player}:{str(self.first_player_score)} \n"
                              f"{self.second_player}:{str(self.second_player_score)}")
                        break
                try:
                    o_choice = tuple(map(int, input("Enter coordinates, where you want to put O \n").split(',')))
                    self.update_cell(o_choice, "O")
                except (ValueError, IndexError):
                    print("Incorrect output!! Coordinates should be inputted in form '1,2'")

                if self.is_winner("O"):
                    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    logging.basicConfig(filename='win_log.txt', filemode='a', level=logging.INFO)
                    logging.info(f"Winner:{self.identify_player('O')}, time:{now}")
                    print(f"{self.identify_player('O')}, O wins\n")
                    play_again = input("Want to play again Y/N? \n").upper()
                    if play_again == "Y":
                        self.reset_field()
                        continue
                    else:
                        print(f"Final score {self.first_player}:{str(self.first_player_score)} \n"
                              f"{self.second_player}:{str(self.second_player_score)}")
                        clean_logs = input("Do you want to clean logs? Y/N \n").upper()
                        if clean_logs == "Y":
                            self.clear_logs()
                        break
        elif play_choice == 'Y':
            username = input("Enter username for first player \n")
            self.set_first_player_username(username)
            self.set_first_player_choice("X")

            while True:

                move = self.find_best_move(self.get_board())
                ai_choice = move
                self.update_cell(ai_choice, "O")
                self.refresh_screen()

                if self.is_winner("O"):
                    print("AI wins")
                    break

                if self.is_draw():
                    print("Draw")
                    break

                while True:
                    try:
                        x_choice = tuple(map(int, input("Enter coordinates, where you want to put X \n").split(',')))
                        cell_count_before = self.get_amount_of_free_cells()
                        self.update_cell(x_choice, "X")
                        cell_count_after = self.get_amount_of_free_cells()
                    except (ValueError, IndexError):
                        cell_count_before = self.get_amount_of_free_cells()
                        cell_count_after = self.get_amount_of_free_cells()
                        print("Incorrect output!! Coordinates should be inputted in form '1,2'")
                    if cell_count_before != cell_count_after:
                        break
                self.refresh_screen()

                if self.is_winner("X"):
                    print(f"X wins {self.get_first_layer_username()}")
                    break


if __name__ == "__main__":
    board = Board()
    board.play()
