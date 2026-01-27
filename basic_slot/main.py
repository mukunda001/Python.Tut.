MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
        bet_amount = input("What would you like to bet? ")
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
    bet = get_bet()
    total_bet = bet * number_of_lines
    print(f"You are betting ${bet} on {number_of_lines} lines. Total bet: ${total_bet}")

main()