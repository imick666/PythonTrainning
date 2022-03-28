# MARK : - Variables, Namming Convention and Types

first_number = 13 # 'int'
second_number = 32.54 # 'float'
first_string = "I'm a string" # 'str'
second_string = 'I\'m another string' # 'str'
first_bool = True # 'bool'
second_bool = False # 'false'

# MARK : - Variables type

print(type(first_number)) # => { class 'int' }
first_number = "13" # first_number now contain a string instead of an int
print(type(first_number)) # => { class< 'str' }
first_number = 13 # Reset type to int

# MARK : - Numeric operators

first_addition = first_number + second_number + 24
print(first_addition) # => 69.53999999999999
first_multiplication = first_addition * 2
print(first_multiplication) # => 139.07999999999998
first_division = first_multiplication / 4
print(first_division) # => 34.769999999999996

# MARK : - Strings operators

first_strings_somme = first_string + second_string
print(first_strings_somme) # => "I'm a stringI'm another string"
second_strings_somme = first_string + " " + second_string
print(second_strings_somme) # => "I'm a string I'm another string"

string_multiplication = first_string * 3
print(string_multiplication) # => "I'm a stringI'm a stringI'm a string"

# MARK: - Boolean operators

first_and_second_bool = first_bool and second_bool
print(first_and_second_bool) # => Flase
first_or_second_bool = first_bool or second_bool
print(first_or_second_bool) # => True
print(not first_or_second_bool) # => False

# MARK : - Comparison

first_bigger_than_second_number = first_number > second_number
print(first_bigger_than_second_number) # => False
first_smaller_than_second_number = first_number < second_number
print(first_smaller_than_second_number) # => True
first_equal_second_number = first_number == second_number
print(first_equal_second_number) # => False
first_bigger_or_equal_second_number = first_number >= second_number
print(first_equal_second_number) # => False
first_different_second_number = first_number != second_number
print(first_different_second_number) # => True

# MARK : - Conversions

string_as_int = int("12")
print(string_as_int) # => 12
int_as_string = str(12)
print(int_as_string) # => "12"
float_as_int = int(12.52)
print(float_as_int) # => 12

# MARK : - Read user's input in console

user_input = input("What's your name? :  ")
print("Your name is : " + user_input) # => "Your name is : { The user's input }"
