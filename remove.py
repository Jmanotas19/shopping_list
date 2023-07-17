def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list")
    else:
        print(f"{item} is not found in the shopping list")
