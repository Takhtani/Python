my_list = [10, 20, 30, 40, 50]
print("Original list      :", my_list)

my_list.append(60)
print("After append(60)   :", my_list)

my_list.insert(2, 25)
print("After insert(2,25) :", my_list)

my_list.extend([70, 80])
print("After extend       :", my_list)

my_list.remove(30)
print("After remove(30)   :", my_list)

print("pop() returned     :", my_list.pop(), "->", my_list)
print("index of 40        :", my_list.index(40))
print("count of 20        :", my_list.count(20))

my_list.sort(reverse=True)
print("Sorted descending  :", my_list)
my_list.reverse()
print("After reverse()    :", my_list)

print("Length, Sum        :", len(my_list), sum(my_list))
print("Min, Max           :", min(my_list), max(my_list))
print("Slice [1:4]        :", my_list[1:4])

copy_list = my_list.copy()
my_list.clear()
print("After clear()      :", my_list)
print("Copy still has     :", copy_list)
