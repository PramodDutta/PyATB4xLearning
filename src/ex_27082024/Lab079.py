my_shoping_list = ["bread", "milk", "butter"]
# To remove the duplicate from the list -> set - data
print(my_shoping_list[0])
print(len(my_shoping_list))


def bring_more_food(my_list):
    more_item = input("Enter the item\n")
    my_list.append(more_item)
    # my_list.remove(more_item)
    # my_list.insert(0, more_item)
    return my_list


l = bring_more_food(my_shoping_list)
print(l)
