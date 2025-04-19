import subprocess

def main_menu():
    while True:
        print("Выберите игру:")
        print("1. Блэкджек")
        print("2. Угадай число")
        print("3. Выход")

        choice = input("Введите номер игры: ").strip()

        if choice == '1':
            subprocess.run(['python', 'blackjack.py'])
        elif choice == '2':
            subprocess.run(['python', 'guesser.py'])
        elif choice == '3':
            print("Выход из игры")
            break
        else:
            print("некорректный ввод, введите только номер игры")

if __name__ == "__main__":
    main_menu()