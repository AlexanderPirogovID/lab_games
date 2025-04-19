import random
import time

start_time = time.time()

def log_action(action):
    elapsed_time = time.time() - start_time
    log_entry = f"{elapsed_time:.2f} секунд: {action}"
    with open("actions.txt", "a", encoding='utf-8') as file:
        file.write(action + "\n")


def guess_the_number():
    attempts = 3
    number_to_guess = random.randint(0, 100)

    log_action("игра началась")
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Попытка {attempt}: введите число: "))
            log_action(f"попытка {attempt}: пользователь ввел {guess}")
        except ValueError:
            print("введите целое число")
            log_action(f"попытка {attempt}: пользователь ввел некорректное значение.")
            continue
        if guess < 0 or guess > 100:
            print("число должно быть от 0 до 100")
            log_action(f"попытка {attempt}: пользователь ввел некорректное значение.")
            continue
        if guess < number_to_guess:
            print("число чуть больше)")
            log_action(f"попытка {attempt}: слишком маленькое число")
        elif guess > number_to_guess:
            print("число чуть меньше)")
            log_action(f"попытка {attempt}: слишком большое число")
        else:
            print(f"да, число было {number_to_guess}")
            log_action(f"пользователь угадал число {number_to_guess}")
            break
    else:
        print(f"вы не угадали, число было {number_to_guess}")
        log_action(f"пользователь не угадал, число было {number_to_guess}")

if __name__ == "__main__":
    guess_the_number()