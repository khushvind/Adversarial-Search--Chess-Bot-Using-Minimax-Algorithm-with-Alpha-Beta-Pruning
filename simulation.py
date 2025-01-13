import chess
import chess.svg
from IPython.display import display, SVG
import ipywidgets as widgets



def run_simulation(bot1, bot2, max_iters = 200):
    board = chess.Board()
    game_moves = [board.copy()]

    iter = 0
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = bot1(board.fen())
        else:
            move = bot2(board.fen())

        iter+= 1
        if iter >= max_iters:
          break

        board.push(move)
        game_moves.append(board.copy())
    return game_moves


# Create a slider to navigate through moves
def show_board(game_moves):
    def update_board(move_number):
        board_size = 700  # Fixed size for the board
        svg_board = chess.svg.board(board=game_moves[move_number], size=board_size)
        svg_output.clear_output(wait=True)
        with svg_output:
            display(SVG(svg_board))
    
    svg_output = widgets.Output()
    
    slider = widgets.IntSlider(
        value=0,
        min=0,
        max=len(game_moves) - 1,
        step=1,
        description='Move:',
        continuous_update=False,
    )
    
    slider.observe(lambda change: update_board(change['new']), names='value')
    
    # Display the slider and the output
    display(slider, svg_output)
    
    # Display the initial board
    update_board(0)