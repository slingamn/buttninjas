def escape_input(input_buffer):
    pieces = input_buffer.split('&amp;')
    return '&amp;'.join(piece.replace('&', '&amp;') for piece in pieces)
