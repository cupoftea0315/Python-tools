# coding: utf-8

my_str = '  LIGAND BASED DRUG DESIGN  '
print(my_str.strip().lower())
print(my_str.strip().lower().capitalize())
print(my_str.strip().lower().title())
print(len(my_str.strip()))

count = 0
for i in my_str:
    count += 1
    my_str = my_str.strip().lower()
    if i == '.':
        my_str[count].upper()
    else:
        my_str[count:].lower()
