class Chess:
    def __init__(self, field=8):
        self.field = field
        self.cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.rows = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.chessboard = [
            ['.' for _ in range(self.field)] for _ in range(self.field)]
        self.figure_moves = [(2, 1), (2, -1), (1, 2),
                             (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

    def output_figure_horse(self, figure_coordinates: str):
        col, row = figure_coordinates[0], figure_coordinates[1]
        i, j = self.rows.index(row), self.cols.index(col)
        figure_place = self.chessboard[i][j] = 'N'
        x, y = None, None

        for y1, x1 in self.figure_moves:
            y = i + y1
            x = j + x1
            if (0 <= x < len(self.chessboard)) and (0 <= y < len(self.chessboard)):
                self.chessboard[y][x] = '*'

        for chess_row in self.chessboard:
            print(*chess_row)


N = input()
ch_dsk = Chess()
ch_dsk.output_figure_horse(N)
