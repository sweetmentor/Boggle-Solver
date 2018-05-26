def make_grid(width, height):
    """
    # 1.Make an empty boggle grid
    2.Creates a grid that will hold all of the tiles for a boggle game and repeat the test
    """
    return {(row, col): ' ' for row in range(height) for col in range(width)} # then repeat the test