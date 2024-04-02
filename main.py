name = input('What is your name? ')
age = input('How old are you? ')
city_life = input('Where do you live? ')

info = f'My name is {name}, im {age} years old, i live in {city_life}'

name_strit = input('What is the name of the street where you live? ')

FLOORS = 9
APARTAMENT_PER_FLOORS = 4
apartament_number = int(input('Enter apartament number: '))
apartament_per_entrance = FLOORS * APARTAMENT_PER_FLOORS
entrance_number = (apartament_number -1) // apartament_per_entrance + 1
print(f'{info}, streeet name : {name_strit} {apartament_number}, Entrance number: {entrance_number}')

