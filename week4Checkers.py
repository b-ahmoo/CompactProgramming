class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = 0
        self.result = None
        self.time = None


class Checker:
    def __init__(self, checkerColor, currentPosition):
        self.checkerColor = checkerColor
        self.currentPosition = currentPosition
        self.isKing = False

class Board:
    def __init__(self):
        self.boardArray = [[None for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                #checkers can be placed on squares where row+col = odd number (check notes for homework for confirmation)
                if (row + col ) % 2 != 0:
                    #first 3 rows for one player
                    if row < 3:
                        self.boardArray[row][col] = Checker("Black", (row,col))

                        #last 3 rows for another player
                    elif row > 4:
                        self.boardArray[row][col] = Checker("Red", (row, col))

    def move_checkers(self, startPosition, endPosition):
        startRow, startCol = startPosition
        endRow, endCol = endPosition

        #move the checker at position boardArray[startRow][startCol] into position boardArray[endRow][endCol]
        self.boardArray[endRow][endCol] = self.boardArray[startRow][startCol]
        self.boardArray[startRow][startCol] = None

    def display_board(self, possibleMoves = None):
        if possibleMoves is None:
            possibleMoves = []

        print("\n  0 1 2 3 4 5 6 7")

        for row in range(8):
            rowString = str(row)+ " "

            for col in range(8):
                coordinates = (row,col)
                checker = self.boardArray[row][col]

                if coordinates in possibleMoves:
                    rowString += "* " #possible move
                elif checker is None:
                    rowString += ". " #empty square

                elif checker.checkerColor == "Black":
                    rowString += "B "
                elif checker.checkerColor == "Red":
                    rowString += "R "
            print(rowString)
        print()

    def get_possible_moves(self, piece):
        possibleMoves = []
        currentRow, currentCol = piece.currentPosition
        if piece.checkerColor == "Black":
            moveRow = 1
        elif piece.checkerColor == "Red":
            moveRow = -1

        else:
            return []

        targetRow = currentRow + moveRow
        targetLeftCol = currentCol -1
        targetRightCol = currentCol +1

        if (targetRow >= 0 and targetRow < 8 ) and (targetLeftCol >= 0 and targetLeftCol < 8):
            if self.boardArray[targetRow][targetLeftCol] is None:
                possibleMoves.append((targetRow, targetLeftCol))

        if (targetRow >= 0 and targetRow < 8 ) and (targetRightCol >= 0 and targetRightCol < 8):
                    if self.boardArray[targetRow][targetRightCol] is None:
                        possibleMoves.append((targetRow, targetRightCol))   
        return possibleMoves 


#a game has players (composition)
class Game():
    def __init__(self, playerOne, playerTwo):

        self.playerOne = Player(playerOne, "Black")
        self.playerTwo = Player(playerTwo, "Red")

        self.board = Board()

        self.currentTurn = self.playerOne #playerOne plays first
        self.totalMoves = 0       

    def start_game(self):

        print(f"\n--- {self.currentTurn.name}'s Turn ({self.currentTurn.color}) ---")

        valid_destinations = [(3, 4), (3, 6)]
        self.board.display_board(possibleMoves=valid_destinations)
    
        
my_board = Board()





blackPiece = Checker("Black", (2,3))
print(my_board.get_possible_moves(blackPiece))
my_board.display_board()

myGame = Game("Tom", "Paul")
myGame.start_game()






                
        