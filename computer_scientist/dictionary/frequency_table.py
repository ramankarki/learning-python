def ft(string):
    text = string.lower()
    ft_table = dict()
    ft_list = []
    for letter in text:
        ft_table[letter] = ft_table.get(letter, 0) + 1
    
    for k,v in ft_table.items():
        ft_list.append((k,v))

    return sorted(ft_list)


data = ft("ThiS is String with Upper and lower case Letters")
for k,v in data:
    if k != " ":
        print(k,v)


############################################################################


def add_fruit(inventory, fruits, quantity=0):
    inventory[fruits] = quantity


new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 35)
print(new_inventory["strawberries"] == 35)


