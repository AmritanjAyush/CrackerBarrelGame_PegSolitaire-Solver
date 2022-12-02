from pathlib import Path
from board_manager import Board, initialize_board_configuration

def dfs_peg(root:(Board), best_score_ref, best_path_ref, path = []):
    if root.score() < best_score_ref[0]:
        best_score_ref[0] = root.score()
        best_path_ref[0] = path
    root.generate_children()
    branch = 0
    if root.score() == 1:
        return path
    for child in root.get_children():
        child_result = dfs_peg(child, best_score_ref, best_path_ref, path + [branch])
        if child_result:
            return child_result
        branch = branch+1
    return False

def print_winning_moves(root:(Board), child_choices:list[int]):
    for child_idx in child_choices:
        root = root.get_children()[child_idx]
        print(child_idx)

def get_winning_moves(root:(Board), child_choices:list[int]):
    moves = []
    for child_idx in child_choices:
        root = root.get_children()[child_idx]
        moves.append(root.move)
    return moves


def solve_board(initial_empty):
    initial_config = initialize_board_configuration(initial_empty)
    board = Board(initial_config)
    best_score = [len(initial_config)]
    best_preformance = [[]]
    move_chain = dfs_peg(board, best_score, best_preformance)
    winning_moves = None
    if move_chain:
        winning_moves = get_winning_moves(board, move_chain)
    else:
        winning_moves = get_winning_moves(board, best_preformance[0])
    return winning_moves
