import random
import time  # just for aesthetics
import os  # to create a skip(clear) function

# Config

inputs = True
set_rounds = 1000  # if not inputs

show_all_rounds = True
show_prize = True  # influence only if show_all_rounds
show_win_move = True  # influence only if show_all_rounds

# Some useful functions

def skip(sec):  # clear the terminal
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    time.sleep(sec)
    return os.system(command)

def try_int(string):  # Prevents errors by improper input
    try:
        int(string)
        return True
    except ValueError:
        return False

def percentage(part, whole):  # Create a percentage result
    pc = 100 * float(part) / float(whole)
    return '{:.2f}'.format(pc)


# Script

while True:
    skip(0)  # create a "new" scene

    # Set Rounds

    def input_rounds():
        global rounds
        rounds = input(" Enter the number of rounds: ")
        while not try_int(rounds):
            print("You can only send integers numbers!")
            input_rounds()
        rounds = int(rounds)
        while rounds < 1 or rounds > 10000:
            print("You can only do rounds between 1 and 10.000!")
            input_rounds()
        if 1 <= rounds <= 10000:  # just to make sure..
            return rounds

    if inputs:
        rounds = input_rounds()
    else:
        rounds = set_rounds

    # Set variables

    doors = ["A", "B", "C"]

    chosen_a, chosen_b, chosen_c = 0, 0, 0
    prize_a, prize_b, prize_c = 0, 0, 0
    opened_a, opened_b, opened_c = 0, 0, 0
    win_change, win_keep = 0, 0
    match_n = 0

    # Create the game

    for i in range(rounds):

        # door choice
        chosen = random.choice(doors)
        if chosen == "A":
            chosen_a += 1
        elif chosen == "B":
            chosen_b += 1
        elif chosen == "C":
            chosen_c += 1

        # random prize
        prize = random.choice(doors)
        if prize == "A":
            prize_a += 1
        elif prize == "B":
            prize_b += 1
        elif prize == "C":
            prize_c += 1

        # match (When the 1º door chosen has the prize)
        if chosen == prize:
            match = True
            match_n += 1
        else:
            match = False

        # open a door (without prize and not the chosen one)
        open_d = doors[:]
        if match:
            open_d.remove(prize)  # and chosen
            opened = random.choice(open_d)
        else:
            open_d.remove(prize)
            open_d.remove(chosen)
            opened = open_d[0]

        if opened == "A":
            opened_a += 1
        elif opened == "B":
            opened_b += 1
        elif opened == "C":
            opened_c += 1

        # keep or change?

        # change
        change_list = doors[:]
        change_list.remove(chosen)
        change_list.remove(opened)
        changed = change_list[0]

        # keep
        kept = chosen

        # win move
        if changed == prize:
            win_move = "change!"
            win_change += 1
        elif kept == prize:
            win_move = "keep!"
            win_keep += 1
        else:
            win_move = ""

        # Interface conditionals (can be disabled in the "config" field)

        # show prize
        if show_prize:
            prize_s = "prize: " + prize + " "
        else:
            prize_s = ""

        # show win move
        if show_win_move:
            win_move_s = win_move
        else:
            win_move_s = ""

        # show all rounds
        all_rounds = f"chosen: {chosen} opened: {opened} {prize_s} {win_move_s}"
        if show_all_rounds:
            print(all_rounds)

    # percentages
    p_keep = percentage(win_keep, rounds)
    p_change = percentage(win_change, rounds)

    # Statistics
    rounds_n = "     Rounds: " + str(rounds)
    chosen_n = f"     Chosen door: A: {chosen_a} B: {chosen_b} C: {chosen_c}"
    prize_n = f"     Prize: A: {prize_a} B: {prize_b} C: {prize_c}"
    opened_n = f"     Opened: A: {opened_a} B: {opened_b} C: {opened_c}"
    matches_n = f"     Match: {match_n}  (When the 1º door chosen has the prize)"

    # "Screen"
    print()
    print(f"Statistics: "
          f"\n   {rounds_n}"
          f"\n   {chosen_n}"
          f"\n   {prize_n}"
          f"\n   {opened_n}"
          f"\n   {matches_n}")
    print()
    print(f"Move to win: "
          f"\n     keep: {win_keep}  -> {p_keep}%"
          f"\n   change: {win_change}  -> {p_change}%")

    # Finish or restart
    finish = input("\n\n\nPress [Enter] to restart... \n Or type 'exit' to leave: ")
    exit_function = ["Exit", "EXIT", "exit", "Leave", "LEAVE", "leave"]
    if finish in exit_function:
        print("\n")
        time.sleep(0.5)
        print("leaving...")
        time.sleep(1)
        exit()
    else:
        print("\n")
        time.sleep(0.5)
        print("restarting...")
        time.sleep(1)
