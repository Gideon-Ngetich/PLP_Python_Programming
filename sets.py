set_1 = set()
set_2 = set()
set_3 = set()

size = int(input('Enter the size of the sets: '))

print('Enter the value of set 1: ')
for value in range(size):
    num = int(input())
    set_1.add(num)
print('The values of set 1: ', set_1)

print('Enter the value of set 2: ')
for value in range(size):
    num = int(input())
    set_2.add(num)
print('The values of set 2: ', set_2)

for i in set_1:
    for j in set_2:
        if(i == j):
            set_3.add(j)

print('The values of set 3: ', set_3)