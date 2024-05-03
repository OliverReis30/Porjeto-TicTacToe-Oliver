import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

def print_board(board):
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("-----------")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("-----------")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))

def main():
    print("Bem-vindo ao Jogo Tic-Tac-Toe!")

    while True:
        board = server.get_board()
        print("Estado atual do tabuleiro:")
        print_board(board)

        position = int(input("Digite a posição (0-8) para fazer sua jogada: "))
        response = server.make_move(position)
        print(response)

        if response.startswith("Vencedor:") or response == "Empate!":
            break

if __name__ == "__main__":
    main()
