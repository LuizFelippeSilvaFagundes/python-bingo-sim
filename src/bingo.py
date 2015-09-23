import random

def op(n):
    log = Winners()
    hall = Game()

    for i in range(1, (n + 1)):
        log.add(hall.play())
        if i % 500 == 0:
            print(i)
            log.echo()

    return log.grab()

class Winners:

    def __init__(self):
        self.records = [{}, {}, {}]
        for i in range(5,87):
            self.records[0][i] = 0
            self.records[1][i] = 0
            self.records[2][i] = 0

    def add(self, calls):
        self.records[0][calls[0]] += 1
        self.records[1][calls[1]] += 1
        self.records[2][calls[2]] += 1

    def echo(self):
        print('|-Calls-|-One Line-|-Two Line-|-Full House-|')
        for i in range(5, 87):
            print("| %s | %s | %s |   %s |" % (str(i).rjust(5), str(self.records[0][i]).rjust(8), str(self.records[1][i]).rjust(8), str(self.records[2][i]).rjust(8)))

    def grab(self):
        return self.records

class Game:

    def __init__(self):
        self.reset()

    def reset(self):
        self.balls = list(range(1,91))
        self.sheet = []
        for i in range(0, 6):
            self.sheet.append([])
            for j in range(0, 3):
                self.sheet[i].append([])
                for k in range(0, 5):
                    self.sheet[i][j].append(0)
        self.lines = 0
        self.shouts = [0, 0, 0]

    def play(self):
        self.reset()
        while self.lines < 3:
            call = self.call()
        return [self.shouts[0], self.shouts[1], self.shouts[2]]

    def calls(self):
        return 90 - len(self.balls)

    def state(self, box):
        lines = 0
        for line in range(0, len(self.sheet[box])):
            if sum(self.sheet[box][line]) == 5:
                lines += 1
        return lines

    def call(self):
        index = random.randint(0, len(self.balls) - 1)
        number = self.balls[index]
        self.balls.remove(number)

        box = (number - 1) // 15
        line = ((number - 1) % 15) // 5
        column = ((number - 1) % 15) % 5

        self.sheet[box][line][column] = 1

        if (self.lines + 1) == self.state(box):
            calls = self.calls()
            self.shouts[self.lines] = calls
            self.lines += 1
            return calls
