
#Write a Python program to convert a given list of strings into list of lists using map function. 

def listed(newitem):
    return (list(newitem))


input_list = []
new_list = []
print("Enter one string per line, press Enter on empty line to finish")

while True:
    entry = input("new string > ").strip()
    if not entry :
        break
    input_list.append(entry)

print(input_list)

result = list(map(listed, input_list))
print(result)

