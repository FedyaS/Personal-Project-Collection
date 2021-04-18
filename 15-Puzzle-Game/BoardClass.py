import random
from enum import Enum
import copy


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Square:
    def __init__(self, value: int, size: int, position: [int, int], offset: [int, int], num_squares: int,
                 color_range: [[int, int, int], [int, int, int]],
                 border: int = None):

        if border is not None:
            self.border = border
        else:
            self.border = 0
        self.value = value
        self.size = size
        self.row = position[0]
        self.column = position[1]
        self.ox = offset[0]
        self.oy = offset[1]
        self.x = self.ox + (self.size * self.column) + (self.border * (self.column + 1))
        self.y = self.oy + (self.size * self.row) + (self.border * (self.row + 1))
        self.rect = [self.x, self.y, self.size, self.size]
        self.center = [int((self.x + (self.size / 2) + 0.5)), int((self.y + (self.size / 2) + 0.5))]

        self.absolute_size = self.size + self.border

        self.num_squares = num_squares
        self.color_range = color_range

        if self.value == 0:
            self.color = [0, 0, 0]
        else:
            self.color = []
            if num_squares == 0:
                num_squares = 1
            ratio = value / num_squares
            for i in range(3):
                diff = self.color_range[1][i] - self.color_range[0][i]
                color_difference = diff * ratio
                color_value = int(self.color_range[0][i] + color_difference + 0.5)
                self.color.append(color_value)

    def calculate_color(self):
        if self.value == 0:
            self.color = [0, 0, 0]
        elif self.color_range[0] == self.color_range[1]:
            self.color = self.color_range[0]
        else:
            self.color = []
            if self.num_squares == 0:  # Ensuring that we don't get division by 0
                ratio = self.value / 1
            elif self.value > self.num_squares:
                ratio = 1
            else:
                ratio = self.value / self.num_squares
            for i in range(3):
                diff = self.color_range[1][i] - self.color_range[0][i]
                color_difference = diff * ratio
                color_value = int(self.color_range[0][i] + color_difference + 0.5)
                self.color.append(color_value)

    def update_all_cords(self):  # Call this whenever changing row or column
        self.x = self.ox + (self.size * self.column) + (self.border * (self.column + 1))
        self.y = self.oy + (self.size * self.row) + (self.border * (self.row + 1))
        self.rect = [self.x, self.y, self.size, self.size]
        self.center = [int((self.x + (self.size / 2) + 0.5)), int((self.y + (self.size / 2) + 0.5))]

    def update_value(self, new_value):
        self.value = new_value
        self.calculate_color()

    def update_position(self, new_row, new_column):
        self.row = new_row
        self.column = new_column
        self.update_all_cords()

    def move(self, direction: Direction):
        if direction == Direction.UP:
            self.row -= 1
        elif direction == Direction.RIGHT:
            self.column += 1
        elif direction == Direction.DOWN:
            self.row += 1
        elif direction == Direction.LEFT:
            self.column -= 1
        self.update_all_cords()


class Board:
    def __init__(self, rows: int, columns: int, empty: int, size: int, offset: [int, int],
                 color_range: [[int, int, int], [int, int, int]], border: int = None, outer_border: int = None):
        self.rows = rows
        self.columns = columns
        self.empty = empty
        self.size = size
        self.ox = offset[0]
        self.oy = offset[1]

        self.num_squares = (columns * rows) - self.empty
        self.all_squares = []
        self.non_zero_squares = 0
        self.color_range = color_range

        if border is None:
            self.border = 0
        else:
            self.border = border

        if outer_border is None:
            self.outer_border = 0
        else:
            self.outer_border = outer_border

        for r in range(rows):
            self.all_squares.append([])
            for c in range(columns):
                self.all_squares[r].append(Square(0, self.size, [r, c], [self.ox, self.oy], self.num_squares,
                                                  self.color_range, border=self.border))
        self.board_width = int((self.outer_border * 2) + ((self.columns + 1) * self.border) + (self.columns * self.size)
                               + 0.5)
        self.board_height = int((self.outer_border * 2) + ((self.columns + 1) * self.border) + (self.columns * self.size)
                                + 0.5)
        self.board_boundaries = [[self.ox, self.oy], [self.ox + self.board_width, self.oy + self.board_height]]
        self.prior_moves = []

    def get_square_values(self):
        values = []
        i = 0
        for row in self.all_squares:
            values.append([])
            for square in row:
                values[i].append(square.value)
            i += 1
        return values

    # Takes nums list and sets the board in order (left to right top to bottom) clearing all previous squares
    # This is a dangerous method, suggested to use a loop and set square by square
    def set_board(self, nums, auto=None):
        self.prior_moves = []
        if auto is not None:
            n = 1
            for r in range(self.rows):
                for c in range(self.columns):
                    if n > self.num_squares:
                        self.all_squares[r][c] = Square(0, self.size, [r, c], [self.ox, self.oy], self.num_squares,
                                                        self.color_range, self.border)
                    else:
                        self.all_squares[r][c] = Square(n, self.size, [r, c], [self.ox, self.oy], self.num_squares,
                                                        self.color_range, self.border)
                    n += 1

            self.non_zero_squares = self.num_squares
        else:
            n = 0
            self.non_zero_squares = len(nums)
            for r in range(self.rows):
                for c in range(self.columns):
                    if n >= len(nums):
                        self.all_squares[r][c] = Square(0, self.size, [r, c], [self.ox, self.oy], self.num_squares,
                                                        self.color_range, self.border)
                    else:
                        self.all_squares[r][c] = Square(nums[n], self.size, [r, c], [self.ox, self.oy],
                                                        self.num_squares, self.color_range, self.border)
                    n += 1

    def add_square(self, value: int, position: [int, int]):
        r = position[0]
        c = position[1]
        self.non_zero_squares += 1
        self.all_squares[r][c] = Square(value, self.size, position, [self.ox, self.oy], self.num_squares,
                                        self.color_range, border=self.border)

    def computer_shuffle(self):
        self.prior_moves = []
        all_cords = []
        temp_squares = []
        for r in range(self.rows):
            for c in range(self.columns):
                all_cords.append([r, c])
                temp_squares.append(self.all_squares[r][c])
        random.shuffle(all_cords)
        for i in range(len(all_cords)):
            r = all_cords[i][0]
            c = all_cords[i][1]
            square = temp_squares[i]
            square.update_position(r, c)
            self.all_squares[r][c] = square

    def reverse_cords(self, r1, c1, r2, c2):
        return [r2, c2, r1, c1]

    def determine_direction(self, r1, c1, r2, c2):
        if r2 < r1:
            direction = Direction.UP
        elif r2 > r1:
            direction = Direction.DOWN
        elif c2 < c1:
            direction = Direction.LEFT
        elif c2 > c1:
            direction = Direction.RIGHT
        else:
            return False
        return direction

    def move(self, r1, c1, r2, c2, bypass=False):
        if self.all_squares[r2][c2].value != 0 and not bypass:
            return False
        else:
            direction = self.determine_direction(r1, c1, r2, c2)
            reverse_direction = self.determine_direction(r2, c2, r1, c1)
            if direction is False:
                return False
            else:
                temp_s1 = copy.deepcopy(self.all_squares[r1][c1])
                temp_s2 = copy.deepcopy(self.all_squares[r2][c2])
                self.all_squares[r1][c1] = 0
                self.all_squares[r2][c2] = 0
                temp_s1.move(direction)
                temp_s2.move(reverse_direction)
                self.all_squares[r1][c1] = temp_s2
                self.all_squares[r2][c2] = temp_s1
                self.prior_moves.append([r1, c1, r2, c2])

                return True

    # Do not use this method, use normal move as it is more reliable
    def move_from_squares(self, s1: Square, s2: Square):
        if s2.value != 0:
            print("Value on empty square error")
            return False
        else:
            r1 = copy.deepcopy(s1.row)
            c1 = copy.deepcopy(s1.column)
            r2 = copy.deepcopy(s2.row)
            c2 = copy.deepcopy(s2.column)

            direction = self.determine_direction(r1, c1, r2, c2)
            reverse_direction = self.determine_direction(r2, c2, r1, c1)
            if direction is False:
                print("Direction error")
                return False
            else:
                print("Gone through")
                s1.move(direction)
                s2.move(reverse_direction)
                copy_s1 = copy.deepcopy(s1)
                self.all_squares[r1][c1] = s2
                self.all_squares[r2][c2] = copy_s1

                return True

    def solve(self):
        pass

    def output_rects(self):
        all = []
        for row in self.all_squares:
            for square in row:
                all.append(square.rect)
        return all

    def output_all_draw_params(self):  # Format: [[rect], color, center, value]
        all = []
        for row in self.all_squares:
            for square in row:
                all.append([square.rect, square.color, square.center, square.value])
        return all

    def determine_square(self, cords: (int, int)):
        x = cords[0]
        y = cords[1]
        for row in self.all_squares:
            first_square = row[0]
            y_range = [first_square.y, first_square.y + first_square.size]

            if y_range[0] <= y <= y_range[1]:
                for square in row:
                    x_range = [square.x, square.x + square.size]
                    if x_range[0] <= x <= x_range[1]:
                        return square
        return False

    def determine_if_in_board_boundaries(self, cords: (int, int)):
        x = cords[0]
        y = cords[1]
        if self.board_boundaries[0][1] <= y <= self.board_boundaries[1][1]:
            if self.board_boundaries[0][0] <= x <= self.board_boundaries[1][0]:
                return True
        return False

    def determine_adjacent_empties(self, active_square: Square):
        active_row = active_square.row
        active_column = active_square.column
        all = []
        ri = 0
        for row in self.all_squares:
            if ri == active_row:
                for square in row:
                    if abs(square.column - active_square.column) == 1:
                        if square.value == 0:
                            all.append(square)
            elif abs(ri - active_row) == 1:
                for square in row:
                    if square.column == active_column:
                        if square.value == 0:
                            all.append(square)
            ri += 1
        return all

    def determine_adjacent_squares(self, row, column):
        unchecked = [[row + 1, column], [row - 1, column], [row, column + 1], [row, column - 1]]
        checked = []
        for adj in unchecked:
            if adj[0] < 0 or adj[0] >= self.rows:
                pass
            elif adj[1] < 0 or adj[1] >= self.columns:
                pass
            else:
                checked.append(adj)
        return checked

    def adjacent_moves(self, r1, c1, adjacent_squares):
        adjacent_moves = []
        for sq in adjacent_squares:
            move = [r1, c1, sq[0], sq[1]]
            adjacent_moves.append(move)
        return adjacent_moves

    def determine_direction_adj_empties(self, active_square: Square, adjacent_empties: [Square]):
        directions = []
        for square in adjacent_empties:
            directions.append(self.determine_direction(active_square.row, active_square.column, square.row,
                                                       square.column))
        return directions

    def determine_crossover(self, active_square: Square, passive_square: Square, square_movement: [int, int]):
        direction = self.determine_direction(active_square.row, active_square.column, passive_square.row,
                                             passive_square.column)
        crossover = 0
        ax = active_square.x + square_movement[0]
        ay = active_square.y + square_movement[1]
        if direction == Direction.UP or direction == Direction.DOWN:
            crossover = 1 - (abs(ay - passive_square.y) / (self.size + self.border))
        elif direction == Direction.RIGHT or direction == Direction.LEFT:
            crossover = 1 - (abs(ax - passive_square.x) / (self.size + self.border))

        return crossover

    def determine_greatest_crossover(self, active_square: Square, passive_squares: [Square],
                                     square_movement: [int, int]):
        crossover = 0
        crossover_square = 0
        for square in passive_squares:
            temp_crossover = self.determine_crossover(active_square, square, square_movement)
            if temp_crossover > crossover:
                crossover = temp_crossover
                crossover_square = square

        return [crossover, crossover_square]

    def find_square_by_value(self, value: int):
        for row in self.all_squares:
            for square in row:
                if square.value == value:
                    return square
        return False

    def fair_shuffle(self):
        self.prior_moves = []
        self.set_board([], auto=True)

        for n in range(100):
            empty_square = self.find_square_by_value(0)
            adj_squares = self.determine_adjacent_squares(empty_square.row, empty_square.column)
            possible_moves = self.adjacent_moves(empty_square.row, empty_square.column, adj_squares)
            new_moves = []
            if self.prior_moves:
                prior_move = self.prior_moves[-1]
            else:
                prior_move = False

            if prior_move:
                r1, c1, r2, c2 = prior_move
                for move in possible_moves:
                    if move != self.reverse_cords(r1, c1, r2, c2):
                        new_moves.append(move)
            else:
                new_moves = possible_moves

            random.shuffle(new_moves)
            next_move = new_moves[0]
            r1, c1, r2, c2 = next_move
            self.move(r1, c1, r2, c2, bypass=True)
        self.prior_moves = []
