import random, pygame

class Logic:

    def __init__(self):
        self.modifier = 0
        self.correct = 0
        self.total = 0
        self.levelUp = True

    def pairGenerator(self, op):
        b = random.randint(0, 10 + self.modifier)
        a = random.randint(0, 10 + self.modifier)

        if op == "dividir":
            b = random.randint(1, 10 + self.modifier)
            a = random.randrange(0, (10 + self.modifier) * b, b)

        if a < b and op == "subtrair":
            a += b

        return a, b

    def incrementModifier(self):
        bonus = self.modifier // 10 + 1
        self.modifier += bonus

    def decreasceModifier(self):
        bonus = self.modifier // 10 + 1
        self.modifier = max(self.modifier - bonus, 0)

    def manualDifficulty(self, command):
        bonus = self.modifier // 10 + 1
        if command == pygame.K_UP:
            self.modifier += bonus
        elif command == pygame.K_DOWN:
            self.modifier = max(self.modifier - bonus, 0)

    def solve(self, a, b, result, op):
        if op == "somar":
            if (a + b == result):
                self.correct += 1
                self.total += 1
                return True
        elif op == "subtrair":
            if (a - b == result):
                self.correct += 1
                self.total += 1
                return True
        elif op == "multiplicar":
            if (a * b == result):
                self.correct += 1
                self.total += 1
                return True
        elif op == "dividir":
            if (a // b == result):
                self.correct += 1
                self.total += 1
                return True
        self.total += 1
        return False