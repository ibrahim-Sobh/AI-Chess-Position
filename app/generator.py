from cairosvg import svg2png
import chess.svg
import chess

def generate_random_image_from_FEN(FEN,optional_path='../random/'):
    board = chess.Board(FEN)
    boardsvg = chess.svg.board(board, size=400,coordinates=False)
    FEN = FEN.replace('/', '-')
    svg2png(bytestring=boardsvg,write_to=optional_path+FEN+'.jpeg')
    return optional_path+FEN+'.jpeg'

