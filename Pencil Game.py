import time
import random

while True:
    try:

        class GAME:
            def __init__(self):
                self.cheated = False
                self.Gameover = False
                self.inputs = False
                while self.inputs == False:
                    self.moves = []  # Initialize record of moves
                    self.range1 = input(
                        "What's the least amount of pencils I can pick? (Default: 1)"
                    )
                    self.range2 = input(
                        "What's the largest amount of pencils I can pick? (Default: 3)"
                    )
                    self.range1 = self.default(self.range1, int(1))  # Default 1 to 1
                    self.range2 = self.default(self.range2, int(3))  # Default 2 to 3
                    if self.range1 > self.range2:
                        print(
                            "Oops!  It seems that your first input was larger than the second!  Don't worry, we have that covered! ;D"
                        )
                        self.temprange = self.range1
                        self.range1 = self.range2
                        self.range2 = self.temprange
                    if int(self.range2) - int(self.range1) < 3 and self.range1 != 1:
                        print("Don't be ridiculous; give me a better range!")
                    else:
                        self.inputs = True
                self.numpencils = input("How many pencils are there? (Default: 15)")
                self.numpencils = self.default(self.numpencils, 15)
                self.originalnumpencils = (
                    self.numpencils
                )  # Set constant to original number
                self.mod = self.range1 + self.range2
                self.first = input("Would you like to go first (y/n)")
                if self.first == "y":  # Only let him move first if he replies correctly
                    print("OK! Let's get started!")
                    time.sleep(0.5)
                    self.pmove()
                else:
                    self.playermove = 0
                    self.makemove(self.playermove)
                    print("No?  OK!")
                    time.sleep(0.5)
                while self.numpencils != 1:  # While game is not over
                    self.playgame()
                for element in range(5, 0, -1):
                    print("Restarting in %s seconds" % element)
                    time.sleep(0.5)

            def default(self, string, value):
                if string == "":
                    return int(value)
                else:
                    return int(string)

            def print_score(self):
                time.sleep(0.5)
                print(
                    "|" * self.numpencils
                    + "   "
                    + str(self.numpencils)
                    + " pencils left!"
                )
                self.checkwin()

            def playgame(self):
                self.checkwin()
                time.sleep(0.5)
                if self.Gameover == False:
                    self.cmove()
                time.sleep(0.5)
                self.checkwin()
                if self.Gameover == False:
                    self.pmove()

            def pmove(self):
                self.playermove = int(input("How many pencils will you take?"))
                if self.playermove not in range(
                    self.range1, self.range2 + 1
                ):  # If not legal move
                    print(
                        "FINE! If you won't play by the rules, I'll change your answer, you blatant cheater!!!"
                    )
                    self.cheated = True
                    self.playermove %= self.mod
                self.makemove(self.playermove)
                time.sleep(0.5)

            def cmove(self):
                self.rem = (self.numpencils - 1) % self.mod
                if self.numpencils > 1:
                    if self.rem == 0:
                        self.rem = random.randint(self.range1, self.range2)
                    self.makemove(self.rem)
                time.sleep(0.5)

            def makemove(
                self, pencilstotake
            ):  # If computer gets first turn, specify in firstmove parameter
                time.sleep(0.5)
                if pencilstotake != 0:
                    self.numpencils -= pencilstotake
                    self.checkgame(
                        str("I take " + str(pencilstotake) + " pencil(s)!"), ("OK!")
                    )
                self.moves.append(pencilstotake)
                time.sleep(0.5)
                self.print_score()
                time.sleep(0.5)
                print(self.moves)

            def checkwin(self):
                if self.numpencils <= 1:
                    if self.numpencils < 1:
                        self.checkgame(
                            ("I guess you took too many pencils.  I win! :D"),
                            ("Looks like I took too many pencils.  You win! :D"),
                        )
                    elif self.numpencils == 1:
                        if self.cheated == True:
                            self.checkgame(
                                (
                                    "I guess you outsmarted me!!! If only you had not cheated, I could congratulate you!"
                                ),
                                (
                                    "Game over! I guess you lost (you blatant cheater), but nice playing with you!"
                                ),
                            )
                        else:
                            self.checkgame(
                                ("I guess you outsmarted me!!! Congratulations!"),
                                (
                                    "Game over! I guess you lost, but nice playing with you!"
                                ),
                            )
                    self.Gameover = True

            def checkgame(
                self, print1, print2
            ):  # print1 if Comp turn, print2 if your turn
                if len(self.moves) % 2 == 1:  # If odd number of elements in record
                    print(str(print1))
                else:
                    print(str(print2))

        GAME()

    except ValueError:
        print("These are not integers!  Don't be silly! ;)")

