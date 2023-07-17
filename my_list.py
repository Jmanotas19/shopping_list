def show_list(shopping_list):
    if shopping_list:
        print("shopping list:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("the shopping list is empty")
