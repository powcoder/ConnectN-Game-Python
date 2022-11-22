https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
class Board(object):

    class Board():

        def __init__(self, n_rows, n_columns, fill_ins, board_name):
            self.n_rows = int(n_rows)
            self.n_columns = int(n_columns)
            self.fill_ins = fill_ins
            self.board_name = str(board_name)
            self.game_board = [[fill_ins] * n_columns for i in
                               range(n_rows)]  # use parameters to set up a board(a list of lists)

        def __str__(self):
            # print board name of the board
            result = ""  # result= string variable
            result += self.board_name + "\n"  # print board name and go to next line

            for i in range(self.n_columns):  # print column index
                result += "\t" + str(i)

            result += "\n"  # goto next line

            for i in range(self.n_rows):
                result += str(i) + "\t"  # index
                result += "\t".join(self.game_board[i])  # board row
                result += "\n"  # to next line
            return result

        def __repr__(self):
            self.__str__()

        def place_character(self, row, column, character):
            # change character
            self.game_board[row][column] = character

        def erase_character(self, row, column):
            self.game_board[row][column] = self.fill_ins

    class BoardsManager():
        def __init__(self):
            self.board_list = []
            self.current_board_idx = -1

        def run(self):
            self.createBoard()
            self.current_board_idx = 0

        def createBoard(self):
            boardname = input("Enter the name of your board: ")
            n_rows = int(input("Enter the number of rows for your board: "))
            n_colums = int(input("Enter the number of columns for your board: "))
            fill_ins = input("Enter the blank character to be used on your board: ")
            new_board = Board(n_rows=n_rows, n_columns=n_colums,
                              fill_ins=fill_ins, board_name=boardname)

            self.board_list.append(new_board)

        def printBoard(self):
            print(self.board_list[self.current_board_idx])

        def interaction(self):
            while True:
                self.printBoard()
                print("Select your action from the list below.")
                print("1. Fill Spot")
                print("2. Erase Spot")
                print("3. Switch Board")
                print("4. Create Board")
                print("5. Quit")

                action = int(input("Enter the number of the action you would like to do: "))  # change input to int
                if action == 1:
                    # Fill Spot
                    character = input("Enter the character you want to add to the board: ")
                    row, col = input("Enter the position to place the character in the form row,col: ").split(
                        ",")  # so we accept all input
                    row = int(row)
                    col = int(col)
                    self.board_list[self.current_board_idx].place_character(row, col, character)

                elif action == 2:
                    # Erase Spot
                    row, col = input("Enter the position you want to erase in the form row, col: ").split(
                        ",")  # so we accept all input
                    row = int(row)
                    col = int(col)
                    self.board_list[self.current_board_idx].erase_character(row, col)
                elif action == 3:
                    # Switch Board
                    for i, board, in enumerate(reversed(self.board_list)):  # reverse list
                        print("%d. %s" % (i, board.board_name))  # print index then board name

                    number = int(input("Enter the number of the board you want to switch to: "))
                    if number < 0 or number >= len(self.board_list):
                        print("Wrong switch number")
                        return
                    self.current_board_idx = len(self.board_list) - number - 1
                elif action == 4:
                    # Create Board
                    self.createBoard()
                elif action == 5:
                    # Quit
                    return
                else:
                    print("Wrong action!!")
                    return
