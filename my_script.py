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