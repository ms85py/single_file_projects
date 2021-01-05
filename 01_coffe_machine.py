
class Coffees:
    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost


espresso = Coffees(250, 0, 16, 4)
latte = Coffees(350, 75, 20, 7)
cappuccino = Coffees(200, 100, 12, 6)


class Machine:
    def __init__(self, comm, water, milk, beans, cups, money):
        self.comm = comm
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money


    def main(self):
        while self.comm != "exit":
            self.comm = input("Write action (buy, fill, take, remaining, exit): ")
            if self.comm == "remaining":
                self.display()
            elif self.comm == "take":
                self.take()
            elif self.comm == "fill":
                self.fill()
            elif self.comm == "buy":
                self.buy()


    def display(self):
        print("\n")
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
        print("\n")


    def take(self):
        print("I gave you", self.money)
        self.money = 0


    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))


    def buy(self):
        buy_stuff = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if buy_stuff == "back":
            self.main()
        elif buy_stuff == "1":
            self.brew(espresso)
        elif buy_stuff == "2":
            self.brew(latte)
        elif buy_stuff == "3":
            self.brew(cappuccino)


    def brew(self, coffee_type):
        if self.cups < 1:
            print("Sorry, not enough cups!")
        elif self.water < coffee_type.water:
            print("Sorry, not enough water!")
        elif self.milk < coffee_type.milk:
            print("Sorry, not enough milk!")
        elif self.beans < coffee_type.beans:
            print("Sorry, not enough beans!")
        else:
            print("I have enough resources, making you a coffee!")
            self.cups -= 1
            self.water -= coffee_type.water
            self.milk -= coffee_type.milk
            self.beans -= coffee_type.beans
            self.money += coffee_type.cost




if __name__ == "__main__":
    instance = Machine("_", 400, 540, 120, 9, 550)
    instance.main()

