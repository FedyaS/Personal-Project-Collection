import unittest
import CubeBasedFigure


class MyTestCase(unittest.TestCase):

    def test_create_simple_cube(self):
        cube = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1]])
        self.assertListEqual([[0, 0, 0], [0, 0, 1]], cube.list_of_cubes_in_figure)

    def test_translate_cord_variant_0(self):
        cube = CubeBasedFigure.Figure([[0, 0, 0]])
        cord = [1, 2, 3]
        expected_cord = [1, 2, 3]
        result = cube.translate_one_cord(cord, 0)
        self.assertListEqual(expected_cord, result)

    def test_translate_cord_variant_1(self):
        cube = CubeBasedFigure.Figure([[0, 0, 0]])
        cord = [1, 2, 3]
        expected_cord = [1, 3, -2]
        result = cube.translate_one_cord(cord, 1)
        self.assertListEqual(expected_cord, result)

    def test_translate_1_cube_positions(self):
        cube = CubeBasedFigure.Figure([[0, 0, 0]])
        expected = [[0, 0, 0]]
        for translation in range(24):
            result = cube.translate_figure(translation)
            self.assertListEqual(expected, result)

    def test_translate_2_cube_figure_position_0(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1]])
        result = figure.translate_figure(0)
        expected = [[0, 0, 0], [0, 0, 1]]
        self.assertListEqual(expected, result)

    def test_translate_3_cube_figure_position_9(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [1, 0, 1]])
        result = figure.translate_figure(9)#option [+y, -x, +z]
        expected = [[0, 0, 0], [0, 0, 1], [0, -1, 1]]
        self.assertListEqual(expected, result)

    def test_get_all_possible_translations(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0]])
        result = figure.get_all_translations()
        expected = [[0, 0, 0]]
        self.assertEqual(len(result), 24)
        for translated_cube in result:
            self.assertListEqual(expected, translated_cube)

    def test_get_grid_coordinates(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1]])
        result = figure.place_in_cube([1, 1, 1], figure.list_of_cubes_in_figure)
        expected = [[1, 1, 1], [1, 1, 2]]
        self.assertListEqual(expected, result)

    def test_get_all_positions_in_cube(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1]])
        result = figure.get_all_positions_in_cube(figure.list_of_cubes_in_figure)
        expected = 27
        self.assertEqual(expected, len(result))

    def test_get_all_positions_all_rotations(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1]])
        result = figure.get_all_positions_all_translations()
        expected = 27*24
        self.assertEqual(expected, len(result))

    def test_get_all_legal_figures(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        result = figure.get_legal_figures()
        for figure in result:
            for cube in figure:
                for coord in cube:
                    self.assertGreaterEqual(coord, 0)
                    self.assertLessEqual(coord, 2)

    def test_figure_difficulty(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        result = figure.difficulty
        expected = 27
        self.assertEqual(expected, result)

    def test_check_combining_two_figures(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        f1 = [[0, 0, 0]]
        f2 = [[0, 0, 0], [0, 0, 1]]
        f3 = [[0, 0, 1], [0, 0, 2]]
        result = [figure.check_combining_two_figures(f1, f2), figure.check_combining_two_figures(f1, f3), figure.check_combining_two_figures(f2, f3)]
        expected = [False, True, False]
        self.assertListEqual(expected, result)

    def test_add_in_new_figure(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        f1 = [[0, 0, 0], [0, 1, 0]]
        f2 = [[0, 1, 0], [1, 1, 0]]
        result = figure.add_in_new_figure(f1, f2)
        expected = [[0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0]]
        self.assertListEqual(expected, result)

    def test_remove_duplicates(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        figs = [[[0, 0, 0], [0, 0, 1]],  [[0, 0, 1], [0, 0, 0]]]
        result = figure.remove_duplicates(figs)
        expected = [[[0, 0, 0], [0, 0, 1]]]
        self.assertListEqual(expected, result)

    def test_remove_two_duplicates(self):
        c000 = [0, 0, 0]
        c001 = [0, 0, 1]
        c002 = [0, 0, 2]
        c101 = [1, 0, 1]
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        figs = [[c000, c001], [c002, c101], [c001, c000], [c101, c002], [c001, c000]]
        result = figure.remove_duplicates(figs)
        expected = [[c000, c001], [c002, c101]]
        self.assertListEqual(expected, result)

    def test_len_no_duplicate_figure_I(self):
        figure = CubeBasedFigure.Figure([[0, 0, 0], [0, 0, 1], [0, 0, 2]])
        legals = figure.get_legal_figures()
        result = figure.remove_duplicates(legals)
        expected = 27
        self.assertEqual(expected, len(result))




if __name__ == '__main__':
    unittest.main()
