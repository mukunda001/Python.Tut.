import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

NO_OF_REELS = 3
NO_OF_ROWS = 3

symbols = ["A", "B", "C", "D"]
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):


def deposit():
    while True:
        amount = input("Enter amount to deposit($):")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
     while True:
        line_no = input(f"Enter number of lines to bet on between 1-{MAX_LINES}: ")
        if line_no.isdigit():
            line_no = int(line_no)
            if 1 <= line_no <= MAX_LINES:
                break
            else:
                print("Number of lines must be greater than zero and less than 4.")
        else:
            print("Please enter a number.")

     return line_no


def get_bet():
    while True:
        bet_amount = input("What would you like to bet on each line? ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a bet amount.")

    return bet_amount


def main():
    balance = deposit()
    number_of_lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * number_of_lines
        if total_bet > balance:
            print(f"You do not have enough balance. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {number_of_lines} lines. Total bet: ${total_bet}")

main()