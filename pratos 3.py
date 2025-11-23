import os

# Создает директорию и файл для статистики
def setup_statistics():
    stats_dir = "game_statistics"
    if not os.path.exists(stats_dir):
        os.makedirs(stats_dir)
    
    stats_file = os.path.join(stats_dir, "tic_tac_toe_stats.txt")
    return stats_file

# Сохраняет статистику игры
def save_statistics(stats_file, winner, moves_count, board_size):
    with open(stats_file, "a", encoding="utf-8") as f:
        f.write(f"Размер поля: {board_size}x{board_size}\n")
        f.write(f"Количество ходов: {moves_count}\n")
        f.write(f"Победитель: {winner}\n")
        f.write("-" * 50 + "\n")

# Создает игровое поле 
def create_table(size): 
    return [['.' for _ in range(size)] for _ in range(size)]

# Выводит игровое поле в консоль 
def print_board(board):
    size = len(board)
    print("   " + " ".join(str(i + 1) for i in range(size)))
    for i in range(size):
        print(f"{i + 1}  " + " ".join(board[i]))
    print()

# Проверяет выиграл ли определеный игрок 
def check_winner(board, player):
    size = len(board)
    for i in range(size):
        # Проверка строк , стобцов и диагоналей
        if all(board[i][j] == player for j in range(size)):
            return True
    
    for j in range(size):
        if all(board[i][j] == player for i in range(size)):
            return True
    
   
    if all(board[i][i] == player for i in range(size)):
        return True
    if all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    
    return False

# Проверяет на заполнение всех клеток на поле после этого выдает ничью
def check_draw(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == '.':
                return False
    return True

def main():
    print("Добро пожаловать в Крестики-нолики!")
    
    stats_file = setup_statistics()
    print(f"Статистика будет сохраняться в файл: {stats_file}")
    
    # Пользователь вводит размер поле и проверяеться на правильный размер
    while True:
        try:
            size = int(input("Введите размер поля (3-9): "))
            if 3 <= size <= 9:
                break
            else:
                print("Неверный размер, попробуйте снова")
        except:
            print("Введите число от 3 до 9")
    
    board = create_table(size)
    current_player = 'X'
    moves_count = 0
    
    print(f"Начинаем игру на поле {size}x{size}!")
    
    # Показывет какой игрок щас ходит и так же если пользователь напишет те координаты и если клетка будет занята
    while True:
        print_board(board)
        print(f"Ход игрока {current_player}. Введите строку и столбец (например: 1 2): ", end="")
        
        try:
            # Получаем координаты от пользователя
            row, col = map(int, input().split())
            row -= 1
            col -= 1
            
            if row < 0 or row >= size or col < 0 or col >= size:
                print("Неверные координаты! Попробуйте снова.")
                continue
                
            if board[row][col] != '.':
                print("Эта клетка уже занята! Выберите другую.")
                continue
            
            # Делаем ход
            board[row][col] = current_player
            moves_count += 1
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                save_statistics(stats_file, f"Игрок {current_player}", moves_count, size)
                break
            
            if check_draw(board):
                print_board(board)
                print("Ничья!")
                save_statistics(stats_file, "Ничья", moves_count, size)
                break
            
            # Меняем игрока
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("Введите два числа через пробел (например: 1 2)")

# Функция для просмотра статистики
def view_statistics():
    stats_file = setup_statistics()
    if os.path.exists(stats_file):
        print("\n--- Статистика игр ---")
        with open(stats_file, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Статистика пока отсутствует.")

# запускает игру
if __name__ == "__main__":
    while True:
        print("\n1 - Начать новую игру")
        print("2 - Посмотреть статистику")
        print("3 - Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            main()
        elif choice == "2":
            view_statistics()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")