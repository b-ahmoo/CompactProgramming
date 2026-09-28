# Write a Python program to sort a list of dictionaries using Lambda.  Original list of dictionaries : [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue’}]  Sorting the List of dictionaries :  [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}] 

def sort_dictionary():
    original =  [{'make': ' Google ', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue' }]
    sorted_dictionary = sorted(original, key = lambda item: int(item["model"]), reverse = True)
    print(sorted_dictionary)


sort_dictionary()