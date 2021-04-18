import unittest
import Solver
import CubeBasedFigure

class MyTestCase(unittest.TestCase):
    def test_sort_by_difficulty(self):
        solver_x = Solver.Solver()

        solver_x.add_figure([[0, 0, 0], [0, 0, 1]])
        solver_x.add_figure([[0, 0, 0]])
        solver_x.sort_by_difficulty()

        result = []
        for fig in solver_x.figures_list:
            figure = fig.list_of_cubes_in_figure
            result.append(figure)

        expected = [[[0, 0, 0]], [[0, 0, 0], [0, 0, 1]]]

        self.assertEqual(expected, result)

    def test_solve(self):
        solver = Solver.Solver()
        f1 = [
                            [0, 0, 0],
                            [0, 0, 1], [0, 0, 2],
                            [0, 1, 0], [0, 2, 0],
                            [1, 0, 0], [2, 0, 0],
                            [0, 1, 1], [0, 1, 2], [0, 2, 1], [0, 2, 2],
                            [1, 0, 1], [2, 0, 1], [1, 0, 2], [2, 0, 2],
                            [1, 1, 0], [1, 2, 0], [2, 1, 0], [2, 2, 0],
                            [1, 1, 1], [1, 1, 2], [1, 2, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2]
                            ]
        solver.add_figure(f1)
        f2 = [[0, 0, 0]]
        solver.add_figure(f2)

        result = solver.solve()
        expected = 2
        self.assertEqual(expected, len(result))


if __name__ == '__main__':
    unittest.main()
