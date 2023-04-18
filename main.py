# Глобальные константы
x = 'x'
o = '0'
empty = ' '
tie = 'Ничья'
num_squares = 9

# Инструкция для игрока
def display_instruct():
  print(
    """
    Добро пожаловать в игру крестики-нолики. Вы будете играть против компьютера. Посмотрим, кто окажется умнее?
    Чтобы сделать ход, введи число от 0 до 8. Числа соответствуют  полям доски- так, как показано ниже: 
    0 | 1 | 2 
    ---------
    3 | 4 | 5 
    ---------
    6 | 7 | 8 
    Ну что, начнем?\n   """
  )

# Подтверждение начала игры
def ask_yes_no(question):
  response = None
  while response not in ('y', 'n'):
    response = input(question).lower()
  return response

# Ввести число для входа
def ask_number(question, low, high):
  response = None
  while response not in range(low, high):
    response = int(input(question))
  return response

# Кто ходит первый
def pieces():
  go_first = ask_yes_no('Выберешь ходить первым? (y/n): ')
  if go_first == 'y':
    print('\nТогда твой первый ход, играешь крестиками.')
    human = x
    computer = 0
  else:
    print('\nТвой ход второй, ходишь ноликами.')
    computer = x
    human = 0
  return computer, human

# Новая игровая доска
def new_board():
    board=[]
    for i in range(num_squares):
        board.append(empty)
    return board

# Отображение игровой доски на экране
def display_board(board):
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6], '|', board[7], '|', board[8], '\n')

# Доступные ходы
def legal_moves(board):
  moves = []
  for square in range(num_squares):
    if board[square] == empty:
      moves.append(square)
  return moves

# Определение победителя
def winner(board):
  ways_to_win = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 3, 6),
                 (1, 4, 7),
                 (2, 5, 8),
                 (0, 4, 8),
                 (2, 4, 6))
  for row in ways_to_win:
    if board[row[0]] == board[row[1]] == board[row[2]] != empty:
      winner = board[row[0]]
      return winner
    if empty not in board:
      return tie
  return None

# Получить ход от игрока
def human_move(board, human):
  legal = legal_moves(board)
  move = None
  while move not in legal:
    move = ask_number('Твой ход. Выбери одно из полей (0-8):', 0, num_squares)
    if move not in legal:
      print('\nЭто поле уже занято. Выбери другое.\n')
  print('Ладно')
  return move

# Ход компьютера
def computer_move(board, computer, human):
  board = board[:]
  best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
  print('Я выберу поле номер', end=' ')
  for move in legal_moves(board):
    board[move] = computer_move
    if winner(board) == computer:
      print(move)
      return move
    board[move] = empty
  for move in legal_moves(board):
    board[move] = human
    if winner(board) == human:
      print(move)
      return move
    board[move] = empty
  for move in best_moves:
    if move in legal_moves(board):
      print(move)
      return move

# Переход хода
def next_turn(turn):
  if turn == x:
    return 0
  else:
    return x

# Поздравление победителя
def congrat_winner(the_winner, computer, human):
  if the_winner != tie:
    print('Три', the_winner, 'в ряд!\n')
  else:
    print('Ничья!\n')
  if the_winner == computer:
    print('Компьютер победил. \n')
  elif the_winner == human:
    print('Игрок победил!\n')
  elif the_winner == tie:
    print('Ничья.\n')

# Основная часть программы
def main():
  display_instruct()
  computer, human = pieces()
  turn = x
  board = new_board()
  display_board(board)
  while not winner(board):
    if turn == human:
      move = human_move(board, human)
      board[move] = human
    else:
      move = computer_move(board, computer, human)
      board[move] = computer
    display_board(board)
    turn = next_turn(turn)
  the_winner = winner(board)
  congrat_winner(the_winner, computer, human)

# Запуск игры
main()
input('\n\nНажмите Enter, чтобы выйти.')