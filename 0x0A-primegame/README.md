# Prime Game

## Description

This project is a simple implementation of a prime number game. The game involves two players, Maria and Ben, who take turns choosing prime numbers from a list. The player who cannot make a move loses the game.

## Files

- `0-prime_game.py`: Contains the prime game.
- `README.md`: This file.

## Requirements

- Python 3.x

## How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/a3ela/0x0A-primegame.git
   ```
2. Navigate to the project directory:
   ```bash
   cd 0x0A-primegame
   ```
3. Run the game:
   ```bash
   python3 0-prime_game.py
   ```

## Rules

1. The game starts with a list of numbers.
2. Players take turns choosing a prime number from the list.
3. When a prime number is chosen, all multiples of that prime number are removed from the list.
4. The player who cannot make a move loses the game.

## Example

Given the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`:

- Player 1 chooses 2, the list becomes `[1, 3, 5, 7, 9]`.
- Player 2 chooses 3, the list becomes `[1, 5, 7]`.
- Player 1 chooses 5, the list becomes `[1, 7]`.
- Player 2 chooses 7, the list becomes `[1]`.
- Player 1 cannot make a move and loses the game.

## Author

- Abela

## License

This project is licensed under the MIT License.
