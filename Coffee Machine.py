class Machine: 
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def status_printer(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable_cups
{self.money} of money""")
        task()

    def buy(self):
        if any(x < 0 for x in [current.water - self.water, current.milk - self.milk, current.beans - self.beans]):
            print('Sorry, not enough resources')
        else:
            current.water -= self.water
            current.milk -= self.milk
            current.beans -= self.beans
            current.cups -= self.cups
            current.money += self.money
            print('I have enough resources, making you a coffee!')
        task()

latte = Machine(350, 75, 20, 1, 7)
espresso = Machine(250, 0, 16, 1, 4)
cappuccino = Machine(200, 100, 12, 1, 6)
current = Machine(400, 540, 120, 9, 550)
action = ''

def options():
    option = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
    if option == '1':
        espresso.buy()
    if option == '2':
        latte.buy()
    if option == '3':
        cappuccino.buy()
    if option == 'back':
        task()

def task():
    global action
    action = input('Write action (buy, fill, take, remaining, exit):\n').casefold().strip()
    if action == 'buy':
        options()
    if action == 'fill':
        fill()
    if action == 'take':
        take()
    if action == 'remaining':
        current.status_printer()

def fill():
    current.water += int(input('Write how many ml of water do you want to add:\n'))
    current.milk += int(input('Write how many ml of milk do you want to add:\n'))
    current.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
    current.cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
    task()

def take():
    print(f'I gave you ${current.money}\n')
    current.money = 0
    task()

while True: 
    if action == 'exit':
        break
    else:
        task()