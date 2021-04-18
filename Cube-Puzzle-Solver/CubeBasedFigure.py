class Figure():
    def __init__(self, list_of_cubes_in_figure):
        self.list_of_cubes_in_figure = list_of_cubes_in_figure
        self.legal_figures = self.get_legal_figures()
        self.clean_figures = self.remove_duplicates(self.legal_figures)
        self.difficulty = len(self.clean_figures)

    def translate_one_cord(self, cord, translation):
        x, y, z = cord
        translations = [
            [+x, +y, +z],
            [+x, +z, -y],
            [+x, -y, -z],
            [+x, -z, +y],

            [-x, +y, -z],
            [-x, +z, +y],
            [-x, -y, +z],
            [-x, -z, -y],

            [+y, +z, +x],
            [+y, -x, +z],
            [+y, +z, -x],
            [+y, +z, +x],

            [-y, +x, +z],
            [-y, +z, -x],
            [-y, -x, -z],
            [-y, -z, +x],

            [+z, -y, +x],
            [+z, +x, +y],
            [+z, +y, -x],
            [+z, -x, -y],

            [-z, -y, -x],
            [-z, +x, -y],
            [-z, +y, +x],
            [-z, -x, +y]
        ]
        new_cord = translations[translation]

        return new_cord

    def translate_figure(self, translation):
        new_figure = []
        for cube in self.list_of_cubes_in_figure:
            new_cube = self.translate_one_cord(cube, translation)
            new_figure.append(new_cube)
        return new_figure

    def get_all_translations(self):
        all_figure_translations = []
        for translation in range(24):
            result = self.translate_figure(translation)
            all_figure_translations.append(result)
        return all_figure_translations

    def place_in_cube(self, new_location, figure):
        new_figure = []
        for cube in figure:
            new_figure.append([cube[i] + new_location[i] for i in range(len(cube))])
        return new_figure

    def get_all_positions_in_cube(self, figure):
        all_figure_positions = []
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    all_figure_positions.append(self.place_in_cube([x, y, z], figure))
        return all_figure_positions

    def get_all_positions_all_translations(self):
        all_positions_all_translations = []
        all_translations = self.get_all_translations()

        for translation in all_translations:
            all_positions_of_translation = self.get_all_positions_in_cube(translation)
            for pos in all_positions_of_translation:
                all_positions_all_translations.append(pos)

        return all_positions_all_translations

    def get_legal_figures(self):
        all_figures = self.get_all_positions_all_translations()
        legal_figures = []

        for figure in all_figures:
            legal = True
            for cube in figure:
                for coord in cube:
                    if not 0 <= coord <= 2:
                        legal = False
            if legal:
                legal_figures.append(figure)
        return legal_figures

    def check_combining_two_figures(self, current_figure, new_figure):
        for current_cube in current_figure:
            for new_cube in new_figure:
                if current_cube == new_cube:
                    return False
        return True

    def add_in_new_figure(self, current_figure, new_figure):
        compiled_figure = current_figure + new_figure
        return compiled_figure

    def remove_duplicates(self, list_figures):
        lf1 = list_figures
        lf2 = list_figures
        duplicate_indices = []

        for if1 in range(len(lf1)):
            for if2 in range(len(lf2)):
                duplicate = True
                for cube in lf1[if1]:
                    if cube in lf2[if2]:
                        pass
                    else:
                        duplicate = False
                        break

                if duplicate:
                    if if1 < if2:
                        if if2 not in duplicate_indices:
                            duplicate_indices.append(if2)

        duplicate_indices.sort(reverse=True)
        for i in duplicate_indices:
            list_figures.pop(i)
        return list_figures