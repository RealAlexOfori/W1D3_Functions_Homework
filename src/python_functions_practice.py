def return_10():
    return 10

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return str(string_1) + str(string_2)

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month):
    months = ["January", "Febuary", "March", "April",
              "May","June","July","August","September","October","November","December"]
    return months[month - 1]

def number_to_short_month_name(month):
    months = ["Jan", "Feb", "Mar", "Apr",
              "May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return months[month - 1]

def volume_of_cube(length) :
    return length ** 3      

def reverse_of_string(string):
    return string[::-1]

def fahrenheit_to_celsius(fahrenheit,celsius):
    return celsius == 5/9 * (fahrenheit - 32) 

