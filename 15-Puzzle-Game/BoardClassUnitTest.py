import unittest
import BoardClass


class MyTestCase(unittest.TestCase):
    def test_4by4_init_squares(self):
        board = BoardClass.Board(4, 4, 0, 10, [0, 0], [[255, 255, 255], [255, 255, 255]])
        self.assertListEqual([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], board.get_square_values())

    def test_set_board_auto(self):
        board = BoardClass.Board(4, 4, 2, 10, [0, 0], [[255, 255, 255], [255, 255, 255]])
        board.set_board([], auto=True)
        self.assertListEqual([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 0]], board.get_square_values())

    def test_set_board_nums(self):
        board = BoardClass.Board(4, 4, 1, 10, [0, 0], [[255, 255, 255], [255, 255, 255]])
        board.set_board([4, 3, 2, 1, 5, 6, 7, 8, 12, 11, 10, 9, 13, 14, 15, 0])
        self.assertListEqual([[4, 3, 2, 1], [5, 6, 7, 8], [12, 11, 10, 9], [13, 14, 15, 0]], board.get_square_values())

    def test_add_square(self):
        board = BoardClass.Board(4, 4, 1, 10, [0, 0], [[255, 255, 255], [255, 255, 255]])
        board.add_square(15, [3, 2])
        expected = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 15, 0]]
        self.assertListEqual(expected, board.get_square_values())

    def test_computer_shuffle(self):
        board = BoardClass.Board(4, 4, 1, 10, [0, 0], [[255, 255, 255], [255, 255, 255]])
        board.set_board([], auto=True)
        values = board.get_square_values()
        board.computer_shuffle()
        self.assertNotEqual(values, board.get_square_values())

    def test_move(self):
        board = BoardClass.Board(4, 4, 1, 10, [0, 0], [[255, 255, 255], [255, 255, 255]])
        board.set_board([], auto=True)
        board.move(3, 2, 3, 3)
        expected = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
        self.assertListEqual(expected, board.get_square_values())

    def test_output_drawing_rects(self):
        board = BoardClass.Board(4, 4, 1, 10, [100, 100], [[255, 255, 255], [255, 255, 255]])
        rects = board.output_rects()
        expected = [
                    [100, 100, 10, 10],
                    [110, 100, 10, 10],
                    [120, 100, 10, 10],
                    [130, 100, 10, 10],
                    [100, 110, 10, 10],
                    [110, 110, 10, 10],
                    [120, 110, 10, 10],
                    [130, 110, 10, 10],
                    [100, 120, 10, 10],
                    [110, 120, 10, 10],
                    [120, 120, 10, 10],
                    [130, 120, 10, 10],
                    [100, 130, 10, 10],
                    [110, 130, 10, 10],
                    [120, 130, 10, 10],
                    [130, 130, 10, 10]
                    ]
        self.assertListEqual(expected, rects)

    def test_output_all_drawing_params(self):
        board = BoardClass.Board(4, 4, 1, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([], auto=True)
        params = board.output_all_draw_params()
        expected = [
            [[100, 100, 10, 10], [7, 7, 7], [105, 105], 1],
            [[110, 100, 10, 10], [13, 13, 13], [115, 105], 2],
            [[120, 100, 10, 10], [20, 20, 20], [125, 105], 3],
            [[130, 100, 10, 10], [27, 27, 27], [135, 105], 4],
            [[100, 110, 10, 10], [33, 33, 33], [105, 115], 5],
            [[110, 110, 10, 10], [40, 40, 40], [115, 115], 6],
            [[120, 110, 10, 10], [47, 47, 47], [125, 115], 7],
            [[130, 110, 10, 10], [53, 53, 53], [135, 115], 8],
            [[100, 120, 10, 10], [60, 60, 60], [105, 125], 9],
            [[110, 120, 10, 10], [67, 67, 67], [115, 125], 10],
            [[120, 120, 10, 10], [73, 73, 73], [125, 125], 11],
            [[130, 120, 10, 10], [80, 80, 80], [135, 125], 12],
            [[100, 130, 10, 10], [87, 87, 87], [105, 135], 13],
            [[110, 130, 10, 10], [93, 93, 93], [115, 135], 14],
            [[120, 130, 10, 10], [100, 100, 100], [125, 135], 15],
            [[130, 130, 10, 10], [0, 0, 0], [135, 135], 0]
        ]
        self.assertListEqual(expected, params)

    def test_board_determine_square(self):
        board = BoardClass.Board(4, 4, 1, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([], auto=True)
        no_square = board.determine_square((0, 0))
        square = board.determine_square((105, 105))
        self.assertEqual(False, no_square)
        self.assertEqual(1, square.value)

    def test_determine_if_in_board_boundaries(self):
        board = BoardClass.Board(4, 4, 1, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([], auto=True)
        out = board.determine_if_in_board_boundaries((0, 0))
        inside = board.determine_if_in_board_boundaries((105, 105))
        self.assertEqual(False, out)
        self.assertEqual(True, inside)

    def test_determine_adjacent_empties(self):
        board = BoardClass.Board(4, 4, 1, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([], auto=True)
        my_square = board.all_squares[3][2]
        adj_empties = board.determine_adjacent_empties(my_square)
        self.assertEqual(0, adj_empties[0].value)
        my_square = board.all_squares[0][0]
        adj_empties = board.determine_adjacent_empties(my_square)
        self.assertEqual([], adj_empties)

    def test_determine_adjacent_squares(self):
        board = BoardClass.Board(4, 4, 1, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([], auto=True)
        expected1 = [[3, 2], [1, 2], [2, 3], [2, 1]]
        result1 = board.determine_adjacent_squares(2, 2)
        self.assertListEqual(expected1, result1)
        expected2 = [[2, 3], [3, 2]]
        result2 = board.determine_adjacent_squares(3, 3)
        self.assertListEqual(expected2, result2)

    def test_determine_direction_adj_empties(self):
        board = BoardClass.Board(1, 3, 2, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([0, 1, 0])
        my_square = board.all_squares[0][1]
        empties = [board.all_squares[0][0], board.all_squares[0][2]]
        dirs = board.determine_direction_adj_empties(my_square, empties)
        self.assertEqual([BoardClass.Direction.LEFT, BoardClass.Direction.RIGHT], dirs)

    def test_determine_crossover(self):
        board = BoardClass.Board(1, 3, 2, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([0, 1, 0])
        active_square = board.all_squares[0][1]
        passive_square = board.all_squares[0][0]
        crossover = board.determine_crossover(active_square, passive_square, [-2, 0])
        expected = 0.2
        self.assertAlmostEqual(expected, crossover)

    def test_determine_greatest_crossover(self):
        board = BoardClass.Board(1, 3, 2, 10, [100, 100], [[0, 0, 0], [100, 100, 100]])
        board.set_board([0, 1, 0])
        active_square = board.all_squares[0][1]
        passive_squares = [board.all_squares[0][0], board.all_squares[0][2]]
        crossover = board.determine_greatest_crossover(active_square, passive_squares, [2, 0])[0]
        expected = 0.2
        self.assertAlmostEqual(expected, crossover)



    def test_square_color_range_init(self):
        square = BoardClass.Square(5, 100, [0, 0], [0, 0], 15, [[0, 0, 0], [30, 60, 90]])
        expected = [10, 20, 30]
        self.assertListEqual(expected, square.color)

    def test_square_color_init(self):
        square = BoardClass.Square(5, 100, [0, 0], [0, 0], 15, [[30, 60, 90], [30, 60, 90]])
        expected = [30, 60, 90]
        self.assertListEqual(expected, square.color)

    def test_square_cords_init(self):
        square = BoardClass.Square(5, 20, [0, 1], [100, 200], 15, [[30, 60, 90], [30, 60, 90]])
        expected = [120, 200, 20, 20]
        self.assertListEqual(expected, square.rect)

    def test_square_update_all_cords(self):
        square = BoardClass.Square(5, 20, [0, 1], [100, 200], 15, [[30, 60, 90], [30, 60, 90]])
        square.column = 2
        square.row = 1
        square.update_all_cords()
        expected = [[140, 220, 20, 20], [150, 230]]
        self.assertListEqual(expected, [square.rect, square.center])

    def test_square_move(self):
        square = BoardClass.Square(5, 20, [0, 1], [100, 200], 15,[[30, 60, 90], [30, 60, 90]], border=1)
        square.move(BoardClass.Direction.LEFT)
        expected = [[101, 201, 20, 20], [111, 211]]
        self.assertListEqual(expected, [square.rect, square.center])


if __name__ == '__main__':
    unittest.main()
