size = int(input('Enter the size of the list: '))

num_list = []

print("Enter integer values")
for i in range(size):
    num = int(input())
    num_list.append(num)

sum_of_numlist = sum(num_list)

print('The sum of the list values is :', sum_of_numlist)