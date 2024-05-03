# Tic-Tac-Toe RPC Game

This is a simple implementation of a Tic-Tac-Toe game using Remote Procedure Call (RPC) in Python. It consists of a server that manages the game state and two clients that can connect to the server to play the game remotely.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
git clone https://github.com/OliverReis30/Porjeto-TicTacToe-Oliver.git

2. Navigate to the project directory:
cd Porjeto-TicTacToe-Oliver

3. Run the server:
python server.py

4. Open another terminal window/tab, navigate to the project directory, and run the client:
python client.py

5. Follow the prompts in the client to make moves and play the game. Enjoy!

## Game Rules

- The game is played on a 3x3 grid.
- Players take turns placing their symbol ('X' or 'O') on an empty cell.
- The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game.
- If all cells are filled without any player winning, the game ends in a tie.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
