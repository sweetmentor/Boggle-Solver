from string import ascii_uppercase
from random import choice # Choice fctn returns an item from a list at random.

def make_grid(width, height):
    """
    # 1.Make an empty boggle grid
    2.Creates a grid that will hold all of the tiles for a boggle game and repeat the test
    """
    # 1.return {(row, col): ' ' for row in range(height) for col in range(width)} # then repeat the test
    return {(row, col): choice(ascii_uppercase) # 2.
        for row in range(height)
        for col in range(width)}

def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    row = coords[0]
    col = coords[1]
    
    # Assign each of the neighbours
    # Top-left to top-right.
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    # left to right
    left = (row, col - 1)
    # The (row, col) coordinates passed to this function are situated here
    right = (row, col + 1)
    
    # Bottom-left to bottom-right
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right, left, right, bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """
    Get all of the possible neighbours for each position in the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string
    """
    return ''.join([grid[p] for p in path])
    
# def word_in_dictionary(word, dict): already served its purpose as searched function is now changed to accessing the set of words directly
#     return word in dict
    
def search(grid, dictionary):
    """
    Search through the paths to locate words by matching strings to words in a dictionary
    """
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)
        if word in full_words:  #m modify this to match with get dictionary function
            paths.append(path)
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
            
    for position in grid:
        do_search([position])
        
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    """
    Load Dictionary file
    """
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            
            for i in range(1, len(word)):
                stems.add(word[:i])
        #return {w.strip().upper() for w in f} modify this to match with the width and just return full words and stem
    return full_words, stems
    
def display_words(words):
    print([word for word in words])
        #print(word)
    print("Found %s words" % len(words))
        
def main():
    """
    This is the function that will run the whole project
    """
    grid = make_grid(6, 6)
    """
    Here you can change your grid from a 3x3 to a 2x2 to test run times
    """
    dictionary = get_dictionary("bogwords.txt")
    words = set(search(grid, dictionary))
    # for word in words:
    #     print(word)
    # print("Found %s words" % len(words))
    display_words(words)

if __name__ == "__main__":     
    
    main()
    