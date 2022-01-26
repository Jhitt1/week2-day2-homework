# Build a shopping cart.
cart_list = []
def main_menu():
    while True:
        print("1 View Shopping Cart")
        print("2 Add Item To Cart")
        print("3 Remove Item From Cart")
        print("4 Exit")
        choice = input("Please Choose One Of The Following : ")
        if choice == "1":
            view_list()       
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            break
        else:
            print("INVALID SELECTION!")
cart_list = []

def view_list():
    print("----Whats In The Cart----")
    for i in cart_list:
        print("* " + i)
        print(" ")

def add_item():
        item = input("Please Enter The Item You Want Placed In Your Cart : ").title()
        cart_list.append(item)
        print(item + " have been added to the cart. ")

def remove_item():
        item = input(" What Would You Like To Remove? ").title()
        cart_list.remove(item)
        print(item + "* " + " Have Been Removed From The Cart")
        print()


main_menu()
