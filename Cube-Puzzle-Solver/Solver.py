import CubeBasedFigure
from operator import itemgetter, attrgetter

class Solver():
    def __init__(self):
        self.figures_list = []
        self.solution = []

    def add_figure(self, figure:CubeBasedFigure.Figure):
        self.figures_list.append(CubeBasedFigure.Figure(figure))

    def sort_by_difficulty(self):
        self.figures_list.sort(key=attrgetter('difficulty'))

    def check_combining_two_figures(self, current_figure, new_figure):
        for current_cube in current_figure:
            for new_cube in new_figure:
                if current_cube == new_cube:
                    return False
        return True

    def add_in_new_figure(self, current_figure, new_figure):
        compiled_figure = current_figure + new_figure
        return compiled_figure


    def merge_two_figures(self, figs1, figs2):
        new_combined_figures = []
        for fig1 in figs1:
            for fig2 in figs2:
                if self.check_combining_two_figures(fig1, fig2):
                    new_combined_figures.append(self.add_in_new_figure(fig1, fig2))

        return new_combined_figures

    def merge_all_figures(self):
        merged = self.figures_list[0].clean_figures
        for i2 in range(1, len(self.figures_list)):
            merged = self.merge_two_figures(merged, self.figures_list[i2].clean_figures)

        return merged

    def solve(self):
        solution = []
        self.sort_by_difficulty()
        try:
            all_solutions = self.merge_all_figures()[0]
        except IndexError:
            return []

        amounts = []
        for fig in self.figures_list:
            amount = len(fig.list_of_cubes_in_figure)
            amounts.append(amount)

        counter = 0
        for am in amounts:
            sol_fig = []
            new_counter = counter+am

            if new_counter == 27:
                sol_fig = all_solutions[counter:]

            else:
                sol_fig = all_solutions[counter:new_counter]

            counter = new_counter
            solution.append(sol_fig)

        return solution
