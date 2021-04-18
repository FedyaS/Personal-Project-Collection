import BoardClass
import pygame
import sys

pygame.init()
pygame.font.init()
width = int((pygame.display.Info().current_w / 1.5) + 0.5)
height = int((pygame.display.Info().current_h / 1.5) + 0.5)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

ROWS = 4
COLUMNS = 4
EMPTY = 1
SIZE = 150
BORDER = 2
OUTER_BORDER = 0
BOARD_WIDTH = int(((COLUMNS + 1) * BORDER) + (COLUMNS * SIZE) + 0.5)
BOARD_HEIGHT = int(((ROWS + 1) * BORDER) + (ROWS * SIZE) + 0.5)
ox = int(((width - ((OUTER_BORDER * 2) + ((COLUMNS + 1) * BORDER) + (COLUMNS * SIZE))) / 2) + 0.5)
oy = int(((height - ((OUTER_BORDER * 2) + ((ROWS + 1) * BORDER) + (ROWS * SIZE))) / 2) + 0.5)
OFFSET = [ox, oy]
COLOR_RANGE = [[60, 130, 240], [60, 200, 240]]
OUTER_BORDER_COLOR = [255, 255, 255]
CROSSOVER_SWAP_RANGE = 0.50


font_in_square_percent = 80
allowed_space = font_in_square_percent * SIZE / 100
font_size = 10
var = True
while var:
    my_font = pygame.font.SysFont('seguisemibold', font_size)
    rendered_size = my_font.size("99")
    for d in rendered_size:
        if d >= allowed_space:
            var = False
        else:
            font_size += 1

board = BoardClass.Board(ROWS, COLUMNS, EMPTY, SIZE, OFFSET, COLOR_RANGE, border=BORDER)
board.set_board([], auto=True)


def cut_max_movement(cords: [int, int], size: int):
    if abs(cords[0]) > size:
        if cords[0] < size:
            cords[0] = -1 * size
        elif cords[0] > size:
            cords[0] = size

    if abs(cords[1]) > size:
        if cords[1] < size:
            cords[1] = -1 * size
        elif cords[1] > size:
            cords[1] = size

    return cords


def allowed_directions_to_movement_cords(directions: [BoardClass.Direction], cords):
    return_cords = [0, 0]
    for direction in directions:
        if direction == BoardClass.Direction.UP:
            if cords[1] < 0:
                return_cords[1] = cords[1]
        elif direction == BoardClass.Direction.DOWN:
            if cords[1] > 0:
                return_cords[1] = cords[1]
        elif direction == BoardClass.Direction.RIGHT:
            if cords[0] > 0:
                return_cords[0] = cords[0]
        elif direction == BoardClass.Direction.LEFT:
            if cords[0] < 0:
                return_cords[0] = cords[0]

    return return_cords


def draw_outer_border():
    points = [[ox, oy], [ox, oy + BOARD_HEIGHT], [ox + BOARD_WIDTH, oy + BOARD_HEIGHT], [ox + BOARD_WIDTH, oy]]
    # rect = [OFFSET, [BOARD_WIDTH, BOARD_HEIGHT]]
    # pygame.draw.rect(screen, OUTER_BORDER_COLOR, rect)
    pygame.draw.lines(screen, OUTER_BORDER_COLOR, True, points)


def draw_from_cords(cords, special_square=None, special_cords=None):  # Format: [[rect], color, center, value]
    moving_draw = False
    if special_square is not None and special_cords is not None:
        moving_draw = True
    for cord in cords:
        if moving_draw:
            if cord[3] == special_square.value:
                rel_x = special_cords[0]
                rel_y = special_cords[1]
        else:
            rel_x = 0
            rel_y = 0

        pygame.draw.rect(screen, cord[1], cord[0])
        number_surface = my_font.render(str(cord[3]), True, [100, 100, 100])
        temp_font_size = my_font.size(str(cord[3]))
        font_x = int(cord[0][0] + ((SIZE - temp_font_size[0]) / 2) + 0.5)
        font_y = int(cord[0][1] + ((SIZE - temp_font_size[1]) / 2) + 0.5)
        screen.blit(number_surface, [font_x, font_y])


def draw_from_squares(all_squares: [[BoardClass.Square]], special_square: BoardClass.Square = None,
                      special_cords: [int, int] = None):
    moving_draw = False
    if special_square is not None and special_square is not False and special_cords is not None:
        moving_draw = True
    for row in all_squares:
        for square in row:
            if moving_draw and square == special_square:
                pass
            else:
                pygame.draw.rect(screen, square.color, square.rect)
                tp = str(square.value)
                if tp == "0":
                    tp = ""
                number_surface = my_font.render(tp, True, [100, 100, 100])
                temp_font_size = my_font.size(tp)
                font_x = int(square.x + ((SIZE - temp_font_size[0]) / 2) + 0.5)
                font_y = int(square.y + ((SIZE - temp_font_size[1]) / 2) + 0.5)
                screen.blit(number_surface, [font_x, font_y])

    if moving_draw:
        rel_x = special_cords[0]
        rel_y = special_cords[1]
        if abs(rel_x) > abs(rel_y):
            rel_y = 0
        elif abs(rel_y) > abs(rel_x):
            rel_x = 0
        else:
            rel_y = 0
            rel_x = 0
        special_rect = [special_square.x + rel_x, special_square.y+rel_y, special_square.size, special_square.size]
        pygame.draw.rect(screen, special_square.color, special_rect)
        number_surface = my_font.render(str(special_square.value), True, [100, 100, 100])
        temp_font_size = my_font.size(str(special_square.value))
        font_x = int(special_square.x + rel_x + ((SIZE - temp_font_size[0]) / 2) + 0.5)
        font_y = int(special_square.y + rel_y + ((SIZE - temp_font_size[1]) / 2) + 0.5)
        screen.blit(number_surface, [font_x, font_y])

            # pygame.draw.rect(screen, square.color, square.rect)
            # number_surface = my_font.render(str(square.value), True, [100, 100, 100])
            # temp_font_size = my_font.size(str(square.value))
            # font_x = int(square.x + ((SIZE - temp_font_size[0]) / 2) + 0.5)
            # font_y = int(square.y + ((SIZE - temp_font_size[1]) / 2) + 0.5)
            # screen.blit(number_surface, [font_x, font_y])


input_mode = False
input_square = False
input_num_consts = [x for x in range(48, 58)]
input_num_values = [x for x in range(10)]
input_value = 0
moving_square = False
adjacent_empties = []
mouse_movement = [0, 0]
square_movement = [0, 0]
while True:
    clock.tick(60)
    screen.fill([50, 50, 50])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            moving_square = False
            if event.key == pygame.K_SPACE:
                #board.computer_shuffle()
                board.fair_shuffle()
            elif event.key == pygame.K_r:
                board.set_board([], auto=True)
            elif event.key == pygame.K_i:
                if input_mode:
                    input_mode = False
                else:
                    input_mode = True
            elif event.key in input_num_consts:
                if input_mode:
                    if input_square:
                        i = input_num_consts.index(event.key)
                        num = input_num_values[i]
                        input_value = (input_value * 10) + num
                        input_square.update_value(input_value)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            moving_square = board.determine_square(event.pos)
            if moving_square:
                adjacent_empties = board.determine_adjacent_empties(moving_square)
        elif event.type == pygame.MOUSEBUTTONUP:
            if moving_square:
                cr_info = board.determine_greatest_crossover(moving_square, adjacent_empties, square_movement)
                if cr_info[0] >= CROSSOVER_SWAP_RANGE:
                    board.move(moving_square.row, moving_square.column, cr_info[1].row, cr_info[1].column)
            if input_mode:
                input_square = board.determine_square(event.pos)
                input_value = 0

            moving_square = False
        elif event.type == pygame.MOUSEMOTION:
            if moving_square:
                if adjacent_empties:  # and board.determine_if_in_board_boundaries(event.pos)
                    mouse_movement[0] += event.rel[0]
                    mouse_movement[1] += event.rel[1]
                else:
                    moving_square = False

    if not moving_square:
        mouse_movement = [0, 0]
        square_movement = [0, 0]
        adjacent_empties = False
    else:
        if not adjacent_empties:
            moving_square = False
        else:
            temp_dirs = board.determine_direction_adj_empties(moving_square, adjacent_empties)
            square_movement = allowed_directions_to_movement_cords(temp_dirs, mouse_movement)
            square_movement = cut_max_movement(square_movement, moving_square.absolute_size)
    #draw_from_cords(board.output_all_draw_params())
    draw_from_squares(board.all_squares, special_square=moving_square, special_cords=square_movement)
    draw_outer_border()

    pygame.display.flip()
