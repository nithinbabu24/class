grocery = ["milk", "bread", "eggs"]

def add_item(item):
    grocery.append(item)

add_item("butter")
print(grocery)

def remove_last_item():
    grocery.pop()

remove_last_item()
print(grocery)

x = lambda item: print("Item:", item)

for i in grocery:
    x(i)

def count_characters(items):
    if not items:   # base case: empty list
        return 0
    return len(items[0]) + count_characters(items[1:])

print(count_characters(["milk", "bread"]))
