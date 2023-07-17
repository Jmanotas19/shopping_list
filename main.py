from item import add_item
from my_list import show_list
from remove import remove_item


def main():
    shopping_list = []
    while True:
        print("\n--- shopping list ---")
        print("1. show shopping list")
        print("2. add item to the list")
        print("3. remove item from the list")
        print("4. exit")
        option = input("enter the option number: ")
        if option == "1":
            show_list(shopping_list)
        elif option == "2":
            item = input("enter the name of the item to add: ")
            add_item(shopping_list, item)
        elif option == "3":
            item = input("enter the name of the item to remove: ")
            remove_item(shopping_list, item)
        elif option == "4":
            print("thanks for using the shopping list!")
            break
        else:
            print("invalid option. please enter a valid number")


if __name__ == "__main__":
    main()
