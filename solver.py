from pathlib import Path
from peg_solver import solve_board
from network_manager import generate_winning_graphic
from board_manager import initialize_board_configuration
import imageio


initial_empty = input('Please input initial empty nodes (space seperated):')
initial_empty = initial_empty.split(' ')
initial_empty = [int(num) for num in initial_empty]

init = initialize_board_configuration(initial_empty)
moves = solve_board(initial_empty)
output_path = Path.cwd().joinpath('Frames')
output_path.mkdir(parents=True, exist_ok=True)
generate_winning_graphic(moves, init)


file_list = sorted(output_path.glob('*.png'))
frames = []
for file in file_list:
    print(file)
    frames.append(imageio.imread(file))
imageio.mimsave('output.gif', frames, duration = 0.75)