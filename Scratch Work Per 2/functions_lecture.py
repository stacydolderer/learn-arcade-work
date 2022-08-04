def print_hello():
    print("hello!")
    
def print_goodbye():
    print("Bye!")
    
def print_number(my_number):
    print(my_number)

def add_numbers(a, b):
    print(a + b)
    
def sum_two_numbers(a, b):
    result = a + b
    return result

def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result
    
def main():
    """ This is my main program function """
    print_hello()
    print_goodbye()
    print_number(33)
    add_numbers(3, 6)
    my_result = sum_two_numbers(22, 15)
    print(my_result)
    six_pack_volume = volume_cylinder(2.5, 5) * 6
    # Pretend you have some code here
    x = 45
    y = 56

    # Wait, how do I print the result of this?
    calculate_average(x, y)



if __name__ == "__main__":
    main()