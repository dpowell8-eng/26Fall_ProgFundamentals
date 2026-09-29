def greet_user(name):
  return (f"Hello {name}! Welcome aboard.")
## returns a greeting message for the user with their name.
message =greet_user("Amara")
print(message)

def rectangle_stats(length, width): ## returns the area and perimerter of a rectangle fiven the length and the with.
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
#
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area, perimeter = rectangle_stats(length, width) 

print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}") 

def check_number(number):## return "even" if the number is even and "odd" if the number is odd.
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a whole number: "))

result = check_number(number) 

print(f"{number} is {result}.") 