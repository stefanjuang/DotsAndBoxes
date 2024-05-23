```markdown
# Dots and Boxes

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Introduction

Dots and Boxes is a classic pencil-and-paper game for two players. Players take turns drawing lines between dots on a grid, aiming to complete boxes. The player who completes the most boxes wins.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Game Rules](#game-rules)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact Information](#contact-information)
8. [Acknowledgments](#acknowledgments)

## Installation

### Prerequisites
- Python 3.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/stefanjuang/DotsAndBoxes.git
   cd DotsAndBoxes
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

### Examples
1. Initialize the game:
   ```python
   from dots_and_boxes import DotsAndBoxes
   game = DotsAndBoxes(5, 5)
   game.display()
   ```

2. Draw a line:
   ```python
   game.draw_line((0, 0), (0, 1))
   game.display()
   ```

3. Reset the game:
   ```python
   game.reset()
   game.display()
   ```

### Screenshots
![Game Board](./Screenshots.png)

## Configuration

You can configure the game board by setting the number of rows and columns when initializing the `DotsAndBoxes` class.

```python
game = DotsAndBoxes(rows, cols)
```

## Game Rules

### Introduction

Welcome to Dots and Boxes! This is a classic pencil-and-paper game for two players. Players take turns drawing lines between dots on a grid, aiming to complete boxes. The player who completes the most boxes wins.

### Components

- **Game Board**: A grid of dots.
- **Lines**: Horizontal and vertical lines that can be drawn between dots.
- **Boxes**: The squares formed by drawing lines between dots.
- **Players**: Two players, each trying to complete more boxes than the other.
- **Scores**: Keeps track of each player's score.

### Setup

1. **Initialize the Game**:
   - The game board is created with a specified number of rows and columns.
   - Each cell in the grid represents a potential box.
   
2. **Reset the Game**:
   - All lines are removed, and the game is reset to its initial state.
   - Scores for both players are set to zero.
   - Player 1 starts the game.

### Gameplay

#### Turn Structure

On your turn, you will:
1. **Draw a Line**: 
   - Select two adjacent dots and draw a line between them (either horizontal or vertical).
   
2. **Check for Completed Boxes**:
   - If drawing the line completes one or more boxes, you score points for each completed box and get another turn.
   - If no boxes are completed, it becomes the other player's turn.

#### Actions

1. **Draw a Line**:
   - Lines can only be drawn between two adjacent dots.
   - Lines can be horizontal or vertical.
   - A line cannot be drawn if it is already present.

2. **Score Points**:
   - Completing a box earns you a point.
   - The box is marked with your player number (1 or 2).

#### Special Rules

- If a line completes any box, the current player gets another turn.
- The game continues until all possible lines are drawn and all boxes are completed.

### Winning the Game

The game ends when all boxes on the board have been completed. The player with the most completed boxes (and thus the highest score) wins the game. If both players have the same score, the game ends in a tie.

### Examples

#### Example Turn

1. **Player 1's Turn**:
   - Player 1 chooses to draw a line from (0, 0) to (0, 1).
   - The line is drawn, but no boxes are completed.
   - It becomes Player 2's turn.

2. **Player 2's Turn**:
   - Player 2 draws a line from (1, 0) to (1, 1).
   - The line is drawn, completing a box.
   - Player 2 scores 1 point and takes another turn.

3. **Next Turn**:
   - Player 2 draws another line from (1, 1) to (1, 2).
   - No boxes are completed, so it becomes Player 1's turn.

#### Completed Box Scenario

1. **Setup**:
   - Player 1 has drawn lines forming three sides of a box:
     - Line from (0, 0) to (0, 1)
     - Line from (0, 1) to (1, 1)
     - Line from (1, 1) to (1, 0)

2. **Action**:
   - Player 2 draws the fourth line from (0, 0) to (1, 0).
   - The box at (0, 0) is completed.
   - Player 2 scores 1 point and takes another turn.

### Advanced Rules

For a more challenging game, you can:
- Use a larger grid to increase the game's complexity.
- Implement time limits for each player's turn to add a strategic element.

### FAQs

**Q: What happens if two players draw lines that do not complete a box?**
- A: The turn simply passes to the next player without any points being scored.

**Q: Can I draw a line that is not adjacent to any existing lines?**
- A: No, lines must be drawn between two adjacent dots only.

**Q: What if I make an invalid move?**
- A: The game will prompt you to make a valid move instead.

## Contributing

### Guidelines
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Acknowledgments

- The inspiration for this project comes from the classic game Dots and Boxes.
- Thanks to all contributors who helped improve this project.
