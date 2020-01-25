import cmath
import datetime

from math import sqrt, pi

def quadratic_formula(a, b, c):
    x_1 = (-b + sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)
    x_2 = (-b - sqrt((pow(b, 2) - 4 * a * c))) / (2 * a)
    return (x_1, x_2)

if __name__ == '__main__':
    x_1, x_2 = quadratic_formula(1, 2, 1)
    print(x_1, x_2)

#01
# TODO do something~~!!!
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky,")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")

#02
now = datetime.datetime.now()
print("Current date and time :")
print(str(now))

#03
radius = input("Input a radius: ")
# Area = 3.14 * pow(float(radius), 2)
Area = pi * pow(float(radius), 2)


print(Area)

#04
first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
reversed_name = last_name.title() + " " + first_name.title()
print(reversed_name)

#05
n = input("Input the integer value n: ")
double_n = n + n
triple_n = n + n + n
sum = int(n) + int(double_n) + int(triple_n)
print(sum)