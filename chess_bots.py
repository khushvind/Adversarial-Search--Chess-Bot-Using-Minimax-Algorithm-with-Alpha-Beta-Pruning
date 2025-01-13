import chess
import chess.engine
import random
from minimax import mini_max, min_val, max_val, piece_val_map


def chess_bot(board_fen):
    # Initialize the board from FEN
    board = chess.Board(board_fen)
    moves_full = list(board.legal_moves)
    moves_sample = random.sample(moves_full, min(len(moves_full), 10))

    # 1. Try to detect checkmate
    for move in moves_full:
        board.push(move)
        if board.is_checkmate():
            board.pop()
            return move
        board.pop()

    # 2. Check for captures of higher-value pieces
    highest_val_capture = None
    highest_val = 0

    for move in moves_full:
        if board.is_capture(move):
            captured_square = move.to_square
            captured_piece = board.piece_at(captured_square)
            if captured_piece:
                captured_value = piece_val_map[captured_piece.piece_type]
                moving_piece = board.piece_at(move.from_square)
                moving_value = piece_val_map[moving_piece.piece_type] if moving_piece else 0

                if captured_value > moving_value and captured_value > highest_val:
                    highest_val_capture = move
                    highest_val = captured_value

    if highest_val_capture:
        return highest_val_capture

    # 3. Use minimax algorithm with a depth of 2
    best_move = None
    best_eval = float('-inf')

    for move in moves_full:
        board.push(move)
        eval_score, _ = mini_max(board, depth=2, maximizing=False)
        board.pop()

        if eval_score > best_eval:
            best_eval = eval_score
            best_move = move

    if best_move is not None:
        return best_move
    else:
        # Check for captures
        for move in moves_sample:
            if board.is_capture(move):
                return move

        # If no capture is found, do a random move
        return random.choice(moves_full)


def chess_bot_random(board_fen):
    board = chess.Board(board_fen)
    moves = list(board.legal_moves)
    return moves[random.randint(0, len(moves)-1)]