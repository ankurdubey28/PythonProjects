import random
from importlib.machinery import all_suffixes

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for col in range(cols):
        column = []
        # li = all_symbols[:]
        for row in range(rows):
            value = random.choice(all_symbols)
            all_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(mat):
    for row in mat:
        print(" | ".join(row))
    print()



def deposit() -> int:
    while True:
        amount = input("Enter your deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a numerical value.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a numerical value.")
    return lines


def get_bet():
    while True:
        amount = input(f"Enter your bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a numerical value.")
    return amount

def check_win(mat,bet,balance,lines):
    count=0
    won_amount=0;
    for row in mat:
        st=set()
        for i in row:
            st.add(i)
        if len(st)==1:
            count+=1;
            won_amount=symbol_count[st.pop()]
    if count==0:
        print(f"You loose,Better luck next time! , updated balance ${balance-bet*lines}")
    else:
        print(f"Hurray you won, updated balance ${balance+won_amount}")


def game(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient balance. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    check_win(slots, bet, balance, lines)

def main():
   while True:
       choice=input("Would you like to play? Y for yes , Q to quit: ").lower()
       if choice.isalpha()=="q":
           print("Thanks for playing")
           break
       elif choice =="y":
           balance = deposit()
           game(balance)


if __name__ == "__main__":
    main()
