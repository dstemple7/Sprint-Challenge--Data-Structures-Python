import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# create a BST node to put the names in
wicked_fast_names = BSTNode("yeet")

# iterate over the names in list 1 and insert them into the node
for i in names_1:
    wicked_fast_names.insert(i)

# iterate over the names in list 2 and if they're already in the node, append them to the duplicates list, else insert them into the node
for i in names_2:
    if wicked_fast_names.contains(i):
        duplicates.append(i)
    else:
        wicked_fast_names.insert(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
