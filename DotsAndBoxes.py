class DotsAndBoxes:
    def __init__(self, rows, cols):
        """
        Initializes the game board with the given number of rows and columns.
        Sets up the grid and box tracking structures.
        """
        self.rows = rows
        self.cols = cols
        self.reset()

    def reset(self):
        """
        Resets the game to its initial state.
        """
        self.grid = [[{'h': False, 'v': False} for _ in range(self.cols)] for _ in range(self.rows)]
        self.boxes = [[None for _ in range(self.cols - 1)] for _ in range(self.rows - 1)]
        self.current_player = 1
        self.scores = {1: 0, 2: 0}
        print("Game reset")

    def draw_line(self, start=None, end=None):
        """
        Draws a line between two points if the move is valid.
        If a box is completed, the player gets another turn.
        
        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        :return: True if the player gets another turn, False otherwise.
        """
        if start is None or end is None:
            print("Error: Missing required positional arguments 'start' and 'end'. Try again.")
            return False

        if not self.is_valid_input(start, end):
            print(f"Invalid input format: start={start}, end={end}. Try again.")
            return False

        if self.is_game_over():
            self.get_winner()
            return False

        print(f"Player {self.current_player} attempting to draw line from {start} to {end}")
        if self.is_valid_move(start, end):
            print(f"Move from {start} to {end} is valid")
            self.update_grid(start, end)
            completed_box = self.check_and_update_boxes(start, end)
            self.display_grid_and_boxes()
            if completed_box:
                print(f"A box was completed by player {self.current_player}. The current player gets another turn.")
                return True  # Player gets another turn
            else:
                self.current_player = 3 - self.current_player
                print(f"No box completed. Switching to player {self.current_player}")
                return False
        else:
            self.print_invalid_move_message(start, end)
            return False

    def is_valid_input(self, start, end):
        """
        Validates the input to ensure it is in the correct format.
        
        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        :return: True if the input is valid, False otherwise.
        """
        return (isinstance(start, tuple) and isinstance(end, tuple) and
                len(start) == 2 and len(end) == 2 and
                all(isinstance(i, int) for i in start + end))

    def is_valid_move(self, start, end):
        """
        Checks if the move between the start and end points is valid.
        
        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        :return: True if the move is valid, False otherwise.
        """
        return (self.is_within_bounds(start, end) and
                self.is_straight_line(start, end) and
                self.is_adjacent(start, end) and
                not self.is_line_already_drawn(start, end))

    def is_within_bounds(self, start, end):
        return (0 <= start[0] < self.rows and 0 <= start[1] < self.cols and
                0 <= end[0] < self.rows and 0 <= end[1] < self.cols)

    def is_straight_line(self, start, end):
        return (start[0] == end[0]) or (start[1] == end[1])

    def is_adjacent(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1]) == 1

    def is_line_already_drawn(self, start, end):
        if start[0] == end[0]:
            return self.grid[start[0]][min(start[1], end[1])]['h']
        else:
            return self.grid[min(start[0], end[0])][start[1]]['v']

    def update_grid(self, start, end):
        """
        Updates the grid to reflect the drawn line.
        
        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        """
        if start[0] == end[0]:
            self.grid[start[0]][min(start[1], end[1])]['h'] = True
            print(f"Horizontal line drawn at row {start[0]} between columns {start[1]} and {end[1]}")
        else:
            self.grid[min(start[0], end[0])][start[1]]['v'] = True
            print(f"Vertical line drawn at column {start[1]} between rows {start[0]} and {end[0]}")

    def check_and_update_boxes(self, start, end):
        """
        Checks if any boxes are completed with the new line and updates the scores.
        
        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        :return: True if a box is completed, False otherwise.
        """
        completed_box = False
        for box in self.get_surrounding_boxes(start, end):
            print(f"Checking potential box completion at {box}")
            if self.is_box_complete(box):
                print(f"Box completed at {box} by player {self.current_player}")
                self.boxes[box[0]][box[1]] = self.current_player
                self.scores[self.current_player] += 1
                completed_box = True
        return completed_box

    def get_surrounding_boxes(self, start, end):
        """
        Returns a list of surrounding boxes that could be affected by the drawn line.
        
        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        :return: List of tuples representing surrounding boxes.
        """
        boxes = []
        if start[0] > 0 and end[0] > 0 and start[0] == end[0]:  # Horizontal line
            boxes.append((start[0] - 1, min(start[1], end[1])))
        if start[0] < self.rows - 1 and end[0] < self.rows - 1 and start[0] == end[0]:  # Horizontal line
            boxes.append((start[0], min(start[1], end[1])))
        if start[1] > 0 and end[1] > 0 and start[1] == end[1]:  # Vertical line
            boxes.append((min(start[0], end[0]), start[1] - 1))
        if start[1] < self.cols - 1 and end[1] < self.cols - 1 and start[1] == end[1]:  # Vertical line
            boxes.append((min(start[0], end[0]), start[1]))
        return boxes

    def is_box_complete(self, box):
        """
        Checks if a given box is complete.
        
        :param box: Tuple (row, col) indicating the box position.
        :return: True if the box is complete, False otherwise.
        """
        r, c = box
        complete = (
            self.grid[r][c]['h'] and self.grid[r + 1][c]['h'] and
            self.grid[r][c]['v'] and self.grid[r][c + 1]['v']
        )
        print(f"Checking box at {box}: horizontal top {self.grid[r][c]['h']}, horizontal bottom {self.grid[r + 1][c]['h']}, vertical left {self.grid[r][c]['v']}, vertical right {self.grid[r][c + 1]['v']}")
        if complete:
            print(f"Box at {box} is complete.")
        return complete

    def is_game_over(self):
        """
        Checks if the game is over by seeing if all boxes are claimed.
        
        :return: True if the game is over, False otherwise.
        """
        for row in self.boxes:
            for box in row:
                if box is None:
                    return False
        return True

    def get_winner(self):
        """
        Determines the winner based on the scores.

        :return: The player number (1 or 2) who has the higher score, or None for a tie.
        """
        print(f"Final Scores: Player 1: {self.scores[1]}, Player 2: {self.scores[2]}")
        if self.scores[1] > self.scores[2]:
            print("Player 1 wins!")
            return 1
        elif self.scores[2] > self.scores[1]:
            print("Player 2 wins!")
            return 2
        else:
            print("It's a tie!")
            return None

    def display(self):
        """
        Displays the current state of the game board and the scores.
        """
        for r in range(self.rows):
            line = ""
            for c in range(self.cols):
                line += "o"
                if c < self.cols - 1:
                    line += "---" if self.grid[r][c]['h'] else "   "
            print(line)
            if r < self.rows - 1:
                line = ""
                for c in range(self.cols):
                    line += "|" if self.grid[r][c]['v'] else " "
                    if c < self.cols - 1:
                        line += "   "
                print(line)
        print("Scores:", self.scores)
        print(f"Player {self.current_player}'s turn.")

    def display_grid_and_boxes(self):
        """
        Displays the current state of the grid and boxes for debugging purposes.
        """
        print("\nGrid state:")
        for r in range(self.rows):
            line = ""
            for c in range(self.cols):
                line += "o"
                if c < self.cols - 1:
                    line += "---" if self.grid[r][c]['h'] else "   "
            print(line)
            if r < self.rows - 1:
                line = ""
                for c in range(self.cols):
                    line += "|" if self.grid[r][c]['v'] else " "
                    if c < self.cols - 1:
                        line += "   "
                print(line)

        print("\nBoxes state:")
        for r in range(len(self.boxes)):
            print(self.boxes[r])
        print("\n")

    def print_invalid_move_message(self, start, end):
        """
        Prints an appropriate error message for an invalid move.

        :param start: Tuple (row, col) indicating the starting point.
        :param end: Tuple (row, col) indicating the ending point.
        """
        if not self.is_within_bounds(start, end):
            print(f"Invalid move by player {self.current_player}: Move is out of bounds. Try again.")
        elif not self.is_straight_line(start, end):
            print(f"Invalid move by player {self.current_player}: Move is not a straight line. Try again.")
        elif not self.is_adjacent(start, end):
            print(f"Invalid move by player {self.current_player}: Move either spans more or less than one unit. Try again.")
        elif self.is_line_already_drawn(start, end):
            print(f"Invalid move by player {self.current_player}: Line is already drawn. Try again.")
        else:
            print(f"Invalid move by player {self.current_player}: Unknown reason. Try again.")


# Test cases to validate the functionality of the DotsAndBoxes game
def run_tests():
    game = DotsAndBoxes(5, 5)

    print("Test 1: Basic Valid Move")
    game.reset()
    assert game.draw_line((0, 0), (0, 1)) == False
    assert game.grid[0][0]['h'] == True
    assert game.grid[0][1]['h'] == False
    print("Test 1 passed")
    print("-" * 40)

    print("Test 2: Invalid Move (Out of Bounds)")
    game.reset()
    result = game.draw_line((5, 5), (5, 6))
    assert result == False
    print("Test 2 passed")
    print("-" * 40)

    print("Test 3: Invalid Move (Diagonal)")
    game.reset()
    result = game.draw_line((0, 0), (1, 1))
    assert result == False
    print("Test 3 passed")
    print("-" * 40)

    print("Test 4: Box Completion")
    game.reset()
    game.draw_line((0, 0), (1, 0))
    game.draw_line((1, 0), (1, 1))
    game.draw_line((1, 1), (0, 1))
    print(f"Before last line - Boxes: {game.boxes}, Scores: {game.scores}")
    assert game.draw_line((0, 0), (0, 1)) == True
    print(f"After last line - Boxes: {game.boxes}, Scores: {game.scores}")
    assert game.boxes[0][0] == 2  # Corrected to player 2
    assert game.scores[2] == 1    # Corrected to player 2
    print("Test 4 passed")
    print("-" * 40)

    print("Test 5: Game Over Check")
    game.reset()
    for r in range(4):
        for c in range(4):
            game.draw_line((r, c), (r, c + 1))
            game.draw_line((r, c), (r + 1, c))
            game.draw_line((r + 1, c), (r + 1, c + 1))
            game.draw_line((r, c + 1), (r + 1, c + 1))
    assert game.is_game_over() == True
    print("Test 5 passed")
    print("-" * 40)

    print("Test 6: Winner Determination")
    assert game.get_winner() == 2  # Player 2 should win because of earlier test
    print("Test 6 passed")
    print("-" * 40)

    print("Test 7: Multiple Boxes Completion")
    game.reset()
    game.draw_line((0, 0), (0, 1))
    game.draw_line((0, 1), (1, 1))
    game.draw_line((1, 1), (2, 1))
    game.draw_line((2, 1), (2, 0))
    game.draw_line((2, 0), (1, 0))
    game.draw_line((1, 0), (0, 0))
    game.draw_line((1, 0), (1, 1))
    print(f"Scores after completing two boxes: {game.scores}")
    assert game.scores[1] == 2
    print("Test 7 passed")
    print("-" * 40)

    print("Test 8: Longer Than 1 Edge Input")
    game.reset()
    game.draw_line((0, 2), (0, 0))
    print("Test 8 passed")
    print("-" * 40)

    print("Test 9: Input A Dot Instead of An Edge")
    game.reset()
    game.draw_line((0, 0), (0, 0))
    print("Test 9 passed")
    print("-" * 40)

    print("Test 11: Drawing Line on Same Edge")
    game.reset()
    assert game.draw_line((0, 0), (0, 1)) == False
    assert not game.draw_line((0, 0), (0, 1))  # Same edge again
    print("Test 11 passed")
    print("-" * 40)

    print("Test 12: Switching Players")
    game.reset()
    assert game.draw_line((0, 0), (0, 1)) == False
    assert game.current_player == 2
    assert game.draw_line((0, 1), (0, 2)) == False
    assert game.current_player == 1
    print("Test 12 passed")
    print("-" * 40)

    print("Test 13: No Input")
    game.reset()
    game.draw_line()
    print("Test 13 passed")
    print("-" * 40)

    print("Test 14: Unexpected Format")
    game.reset()
    game.draw_line(('a',1),(0,0))
    print("Test 14 passed")
    print("-" * 40)

run_tests()