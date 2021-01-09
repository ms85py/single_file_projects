import random


class RPSGame:
    def __init__(self, player_scores, highscore, name, user_choice, pc_choice, deck):
        self.player_scores = player_scores
        self.highscore = highscore
        self.name = name
        self.user_choice = user_choice
        self.pc_choice = pc_choice
        self.deck = deck


    def new_choice(self):
        return random.choice(self.deck)


    def get_create_file(self):
        with open("rating.txt", "r+") as file:
            for entry in file:
                self.player_scores[entry.split()[0]] = int(entry.split()[1])


    def update_write(self, name):
        self.player_scores[name] = self.highscore
        with open("rating.txt", "w") as file_write:
            for key, value in self.player_scores.items():
                print(key, value, file=file_write, sep=" ", end="\n")

    def get_score(self, name):
        if name in self.player_scores.keys():
            self.highscore = self.player_scores.get(name)
        else:
            self.highscore = self.highscore


    def main(self):
        self.name = input("Enter your name: \n")
        print(f"Hello, {self.name}!\n")
        self.get_create_file()
        self.get_score(self.name)
        print("Either enter your own deck or just hit Enter to continue with the normal deck.")
        print("If providing your own deck, please do so in the format of e.g. 'rock, paper, scissors'")
        provided = input().replace(' ', '')
        if not provided:
            self.deck = ["rock", "paper", "scissors"]
            self.pc_choice = self.new_choice()
            print(f"Okay, starting with the normal deck of {self.deck}.\nJust type your choice and hit Enter.")
            print("You can also use the command !rating to see your rating and !exit to quit.\n")
            self.menu()
        else:
            self.deck = provided.split(',')
            self.pc_choice = self.new_choice()
            print(f"Okay, starting with the deck {self.deck}.\nJust type your choice and hit Enter.")
            print("You can also use the command !rating to see your rating and !exit to quit.\n")
            self.menu()


    def process_deck(self, choice):
        after = self.deck.index(choice) + 1
        before = self.deck.index(choice)
        new = self.deck[after:] + self.deck[:before]
        sliced = int(len(new) / 2)
        gets_beaten = new[:sliced]
        return gets_beaten


    def menu(self):
        playing = True
        while playing:
            self.user_choice = input()
            if self.user_choice == "!exit":
                print("Highscore was saved. Thanks for playing!\n")
                playing = False
            elif self.user_choice == "!rating":
                self.get_score(self.name)
                print(self.highscore)
            elif self.user_choice not in self.deck and self.user_choice not in ("!exit", "!rating"):
                print("Sorry, I don't understand. Please try again.\n")
            else:
                self.game(self.user_choice)


    def game(self, choice):
        gets_beaten = self.process_deck(choice)
        if self.user_choice == self.pc_choice:
            print(f"There is a draw. Computer chose ({self.pc_choice})\n")
            self.pc_choice = self.new_choice()
            self.highscore += 50
            self.update_write(self.name)
        elif self.pc_choice in gets_beaten:
            print(f"Sorry, but computer chose {self.pc_choice} and won.\n")
            self.pc_choice = self.new_choice()
        else:
            print(f"Well done. Computer chose {self.pc_choice} and lost.\n")
            self.pc_choice = self.new_choice()
            self.highscore += 100
            self.update_write(self.name)


if __name__ == "__main__":
    instance = RPSGame({}, 0, "", "", "", [])
    instance.main()
