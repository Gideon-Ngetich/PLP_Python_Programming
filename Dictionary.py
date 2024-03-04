personal_info = {}

personal_info['Name'] = input('Enter your name: ')
personal_info['age'] = input('Enter your age: ')
personal_info['Favourite_color'] = input('Enter you favourite color: ')

for key,value in personal_info.items():
    print(key + ': ' + value)