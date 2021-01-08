hello_file = open('hello.txt', 'w')
ga_intro = 'Welcome to General Assembly'
hello_file.write(ga_intro)
# print(hello_file.read())
hello_file.close()

car_file = open('car.txt', 'w')
new_car_list = 'electric\ngas\nhybrid'
car_file.write(new_car_list)
# print(car_file.read())
car_file.close()

with open('food.txt') as foods:
    foods_list = foods.readlines()
    for each_food in foods_list:
        print(each_food)

person_file = open('person.txt', 'w')
person_file.write('Jackson Reeves')
person_file.close()

person_file = open('person.txt')
print(person_file.read())
person_file.close()

with open('person.txt', 'w') as happy_times_file:
    happy_times_file.write('Happy Fun Times!')

with open('person.txt', 'a') as more_file:
    more_file.write('\nAll of it!')

with open('person.txt', 'r+') as this_file:
    print(this_file.read())
    this_file.write('\nI feel all the things')
    print(this_file.read())