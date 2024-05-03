from xmlrpc.server import SimpleXMLRPCServer

class TicTacToeServer:
    def __init__(self):
        self.board = [' '] * 9  # Tabuleiro vazio
        self.current_player = 'X'  # Começa com o jogador X
        self.winner = None

    def get_board(self):
        return self.board

    def make_move(self, position):
        if self.winner:
            return "O jogo já acabou. Vencedor: {}".format(self.winner)

        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                return "Vencedor: {}".format(self.current_player)
            elif ' ' not in self.board:
                return "Empate!"
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                return "Jogada feita. Próximo jogador: {}".format(self.current_player)
        else:
            return "Posição já ocupada. Tente novamente."

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' '):
                return True
        return False

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(TicTacToeServer())
print("Servidor Tic-Tac-Toe RPC iniciado na porta 8000...")
server.serve_forever()
