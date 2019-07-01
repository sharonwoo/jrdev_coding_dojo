'''
class Minesweeper takes the following inputs:
    cols: size of grid -- cols
    rows: size of grid -- rows
    mines: a list of lists specifying where your mines are
        [(0,0),(1,1)] -- there are two mines at 0,0 and 1,1

'''


class Minesweeper:
    def __init__(self, cols, rows, mines=[]):
        self.cols = cols
        self.rows = rows
        self.mines = mines
        pass

    def minesweeper(self):
        '''
        grid:   returns a list of lists of the
                layout of the minesweeper grid
        board:  returns a list of lists of the
                proximity of each cell to mines

        '''

        grid = [
            ['.' for x in range(self.cols)]
            for y in range(self.rows)
        ]

        # modify the grid for placement of mines
        for mine in self.mines:
            row = mine[0]
            col = mine[1]
            grid[row][col] = '*'

        board = None

        # todo: generate list of lists of mine positioning 




        if grid == []:
            return None, None
        else:
            return grid, board
