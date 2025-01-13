import chess
import chess.engine
import random

# Piece values
piece_val_map = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def eval_position(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_val_map[piece.piece_type]
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
    return score

def max_val(board, depth, alpha, beta):
    if board.is_game_over():
        if board.is_checkmate():
            return -float('inf'), None
        return 0, None
    elif depth == 0:
        return eval_position(board), None

    best_val = float('-inf')
    best_move = None

    for move in board.legal_moves:
        board.push(move)
        val, _ = min_val(board, depth - 1, alpha, beta)
        board.pop()

        if val > best_val:
            best_val = val
            best_move = move
        alpha = max(alpha, best_val)
        if alpha >= beta:
            break

    return best_val, best_move

def min_val(board, depth, alpha, beta):
    if board.is_game_over():
        if board.is_checkmate():
            return float('inf'), None
        return 0, None
    elif depth == 0:
        return eval_position(board), None

    best_val = float('inf')
    best_move = None

    for move in board.legal_moves:
        board.push(move)
        val, _ = max_val(board, depth - 1, alpha, beta)
        board.pop()

        if val < best_val:
            best_val = val
            best_move = move
        beta = min(beta, best_val)
        if alpha >= beta:
            break

    return best_val, best_move

def mini_max(board, depth, maximizing):
    alpha = float('-inf')
    beta = float('inf')

    if board.is_game_over():
        if board.is_checkmate():
            return -float('inf') if maximizing else float('inf'), None
        return 0, None

    if maximizing:
        return max_val(board, depth, alpha, beta)
    else:
        return min_val(board, depth, alpha, beta)