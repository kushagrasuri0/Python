print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
chess_pieces = {
    'K': 'King',
    'Q': 'Queen',
    'R': 'Rook',
    'B': 'Bishop',
    'N': 'Knight',
    'P': 'Pawn'
}

def validate_chess_dict(chess_dict):
    valid_keys = set(chess_pieces.keys())
    for key in chess_dict.keys():
        if key not in valid_keys:
            return False
    return True

chess_dict = {
    'K': 1,
    'Q': 1,
    'R': 2,
    'B': 2,
    'N': 2,
    'P': 8
}

is_valid = validate_chess_dict(chess_dict)
print(is_valid)
