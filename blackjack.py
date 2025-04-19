import random

def log_action(action):
    with open("actions_bj_game.txt", "a", encoding='utf-8') as file:
        file.write(action + "\n")

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = ranks * 4
    random.shuffle(deck)
    return deck
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11
        else:
            value += int(card)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    log_action("игра в блэкджек началась")
    print(f"игрок: {player_hand} (стоимость: {calculate_hand_value(player_hand)})")
    print(f"дилер: {dealer_hand[0]}")





    while True:
        action = input("введите 'h' для взятия карты или 's' для удержания: ").strip().lower()
        log_action(f"игрок выбрал действие: {'взять карту' if action == 'h' else 'остановиться'}")

        if action == 'h':
            player_hand.append(deck.pop())
            print(f"игрок: {player_hand} (стоимость: {calculate_hand_value(player_hand)})")
            if calculate_hand_value(player_hand) > 21:
                print("перебор, игрок проиграл")
                log_action("игрок проиграл из-за перебора")
                return
        elif action == 's':
            break
        else:
            print("некорректный ввод, введите 'h' или 's'")




    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"дилер: {dealer_hand} (стоимость: {calculate_hand_value(dealer_hand)})")



    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("игрок выиграл")
        log_action("игрок выиграл")
    elif player_value < dealer_value:
        print("дилер выиграл")
        log_action("дилер выиграл")
    else:
        print("ничья")
        log_action("ничья")


if __name__ == "__main__":
    blackjack()