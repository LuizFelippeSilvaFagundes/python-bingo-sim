import sqlite3
import bingo
import time

def print_results():
    print()
    print('|-Calls-|-One Line-|-Two Line-|-Full House-|')
    for i in range(1, 86):
        print("| %s | %s | %s |   %s |" % (str(i).rjust(5), str(results[0][i]).rjust(8), str(results[1][i]).rjust(8), str(results[2][i]).rjust(8)))

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        print("Please enter an integer")
        return False

def run_game():
    game = bingo.Game()
    while game.lines < 3:
        call = game.call()
    results[0][game.shouts[0]] += 1
    results[1][game.shouts[1]] += 1
    results[2][game.shouts[2]] += 1

if __name__ == '__main__':
    connection = sqlite3.connect('bingo.db')
    connection.row_factory = sqlite3.Row
    c = connection.cursor()

    results = [{},{},{}]

    for row in c.execute("SELECT * FROM results"):
        results[0][row['calls']] = row['one_line']
        results[1][row['calls']] = row['two_line']
        results[2][row['calls']] = row['full_house']

    num_games = input("How many cards do you want to simulate? ")

    if(is_number(num_games)):
        startTime = time.time()

        for i in range(0, int(num_games)):
            run_game()
            if i % 500 == 0:
                print_results()

        endTime = time.time()
        workTime =  endTime - startTime

        for i in range(1, 91):
            c.execute("UPDATE results SET one_line = %d, two_line = %d, full_house = %d WHERE calls = %d" % (results[0][i], results[1][i], results[2][i], i))

        connection.commit()

        print("The results of the bingo game have been added to the database.")
        print("The bingo simulation took %s seconds to complete" % str(workTime))
