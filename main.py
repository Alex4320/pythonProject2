import textwrap

board = list(range(1,10))
rools = 'Крестики-нолики — это очень древняя и интересная игра. Цель — поставка в один ряд три крестика или нолика и не дать своему сопернику сделать то же самое. Участники по очереди ставят на свободные клетки поля знаки. Один играет крестиками, второй — ноликами. Обычно начинает ходить участник, ставящий крестики. Выигрывает тот, кто первым выстроит в ряд 3 свои фигуры по вертикали, горизонтали или диагонали. Крестики-нолики не только занимательное развлечение, но и развивающая игра. У детей она способствует развитию тактического и стратегического мышления, а также интуиции — ребята учатся предугадывать действия соперника.'
def Game_board(board):
    print ("-" * 13)
    for i in range(3):
        print (f'| {board[0 + i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print ("-" * 13)

def launch():
    print(f'Добро пожаловать в игру "Крестики-Нолики"')
    print('Выберете интересующий Вас пункт меню:\n1) Начать игру\n2) Как играть?')
    Chose = input('Ввод: ')

    if Chose == '1':
        main(board)
    elif Chose == '2':
        print(textwrap.fill(rools, 50))
        print('_________________')
        input(f'Нажмите Ввод для возврата в стартовое меню')
        launch()
    else:
        print('Некорректный ввод')
        print('_________________')
        input(f'Нажмите Ввод для возврата в стартовое меню')
        launch()

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Игрок " + player_token+" делает свой ход:")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Пожалуйста, введите число")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Это поле уже занято")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        Game_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (f'Игрок {tmp} выиграл!')
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    Game_board(board)

launch()