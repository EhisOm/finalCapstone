class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}'


shoeList = []

# Function to open and read the inventory.txt file 
def read_shoes_data():
    try:
        with open('inventory.txt', 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                country, code, product, cost, quantity = line.strip().split(',')
                cost = float(cost)
                quantity = int(quantity)
                shoeList.append(Shoes(country, code, product, cost, quantity))
    except Exception as e:
        print(f"Error: {e}.")

# Function to allow a user capture data about shoe 
def capture_shoes():

    if shoeList:
        country = input(f"Please enter the country:")
        code = input(f"""Enter the shoes code:
                    \nIn the format of SKU00000):""")
        product = input(f"Please Enter the product name:")
        cost = float(input(f"Please enter the cost:"))
        quantity = int(input(f"Enter the quantity of shoes:"))
        shoeList.append(Shoes(country, code, product, cost, quantity))
        with open('inventory.txt', 'a', encoding='utf-8-sig') as f:
            f.write(f"\n{country},{code},{product},{cost},{quantity}")


def view_all():
    if shoeList:
        for shoes in shoeList:
            print(f"\t{shoes.country}, {shoes.code}, {shoes.product}, {shoes.cost}, {shoes.quantity}")


def re_stock():
    if shoeList:
        shoes_to_restock = []
        for i in range(5):
            min_quantity = float('inf')
            restock_shoe = None
            for shoes in shoeList:
                if shoes.get_quantity() < min_quantity and shoes not in shoes_to_restock:
                    min_quantity = shoes.get_quantity()
                    restock_shoe = shoes
            if restock_shoe:
                shoes_to_restock.append(restock_shoe)
        if shoes_to_restock:
            print(f"Current the 5 below shoes have the lowest quantity:")
            for i, shoes in enumerate(shoes_to_restock):
                print(f"{i + 1}, {shoes.code}, {shoes.product}, {shoes.quantity}")
            reference = input("Which shoes would you like to restock?:")
            if not reference.isdigit() or int(reference) > len(shoes_to_restock) or int(reference) <= 0:
                print(f"Invalid reference number, try again.")
                return
            chosen_shoe = shoes_to_restock[int(reference) - 1]
            quantity = input(f"enter the quantity of \'{chosen_shoe.product}\' shoes to add: ")
            chosen_shoe.quantity += int(quantity)
            with open('inventory.txt', 'w', encoding='utf-8-sig') as f:
                f.write("country,code,product,cost,quantity\n")
                for shoes in shoeList:
                    f.write(f"{shoes.country},{shoes.code},{shoes.product},{shoes.cost},{shoes.quantity}\n")
        else:
            print(f"No shoes to re-stock.")


def search_shoe():
    if shoeList:
        code = input(f"Enter the shoes code to search (in the form of: SKU00000): ")
        print(f"The below shoes have been found with the code \'{code}\':")
        shoes_found = False
        for shoes in shoeList:
            if shoes.code == code:
                shoes_found = True
                print(f"Country: {shoes.country}\n"
                      f"Code:  {shoes.code}\n"
                      f"Product: {shoes.product}\n"
                      f"Cost (R ): {shoes.cost}\n"
                      f"Stock (units): {shoes.quantity}")
                break
        if not shoes_found:
            print(f"Shoes with code '{code}' not found.")


def value_per_item():

    if shoeList:
        total_value = 0
        print(f"Values for the Shoes items in stock:")
        for shoes in shoeList:
            value = shoes.get_cost() * shoes.get_quantity()
            print(f" {shoes.code},{shoes.product},{shoes.quantity}  x  {shoes.cost}  =  {value}")
            total_value += value
        print(f"Total stock value (R):':{total_value}")


def highest_qty():
    if shoeList:
        max_qty = 0
        max_shoe = None
        for shoes in shoeList:
            if shoes.get_quantity() > max_qty:
                max_qty = shoes.get_quantity()
                max_shoe = shoes
        if max_shoe:
            
            print("\n====== YOUR SHOES WITH THE HIGHEST QUANTITY.=====") 
            print(f"\t\t{max_shoe.product}, {max_shoe.get_quantity()}")
            print("=================================================\n")
        else:
            print(f"No shoes found.")


while True:
    print("\n==========Main Menu=============")
    print("1. - Read shoes data from file")
    print("2. - Register new shoes data")
    print("3. - View all shoes data")
    print("4. - Update shoes quantity")
    print("5. - Search for shoes")
    print("6. - Cost values for each product")
    print("7. - Highest quantity of shoes")
    print("8. - Exit")

    choice = int(input('Enter your choice: '))
    if choice == 1:
        read_shoes_data()
        print("\nYou have succefully loaded the file.")
    elif choice == 2:
        capture_shoes()
    elif choice == 3:
        print("\n=================== YOUR SHOES DISPLAY.========================\n")
        view_all()
        print("\n===============================================================\n")
    elif choice == 4:
        re_stock()
    elif choice == 5:
        search_shoe()
    elif choice == 6:
        value_per_item()
    elif choice == 7:
        highest_qty()
        
    elif choice == 8:
        break
    else:
        print(f"Try again.")

Shoes()