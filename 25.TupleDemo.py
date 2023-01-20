# WAP TO CREATE TUPPLE

length = int(input("Enter a length of dictionary: "))
lst = list()

for i in range(length):
    lst.append(f"val {i + 1}")
tpl = tuple(lst)
print("Tuple is :", tpl)