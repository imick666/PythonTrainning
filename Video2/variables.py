# MARK : - Variables
#       MARK : Namming conventions
#           In python, variables and methodes names must respect the Snake Case convention
#           Each world must be lowercased and seperated with an underscore
#           ex : my_variables_name
#
#       MARK : - Variables types
#           In python, variable are mutables. A variable containning an int can be replace by another type
#
# MARK : - Types
#   - int : Integer number
#   - flaot : Decimal number
#   - str : string of characters
#   - bool : True or False value
#   
#   MARK : -Conversions
#       For convert a typoe in another equivalent, use the type constructor. ex : int("12") => 12
#
# MARK : - Operators
#   MARK: - Numeric operators
#       - + : Make an addition
#       - * : Make a multiplication
#       - / : Make a division
#   MARK : - Strings operators
#       - + : Conquer strings. WARNING : You can't conquer string with other types!
#       - * : Print as many time as the operand the string
#   MARK: - Bollean operators
#       - and : Return True if and only if all variables are True 
#       - or : Return True if one or more variables are True
#       - not : Placed before the value, it return the inverse of the value
#   MARK : - Comparisons
#       - == : Return True if the first value is equal to second value
#       - != : Return True if first value is different than the second value
#       MARK : - Numbers
#           - > : Return True if the first value is biger than de second value
#           - < : Return True if the first value is smaller than the second value
#           - >= or <= : Return True if the first value is bigger/smaller Or equal than the second value
#
# MARK : - Read a user's input in the console
#   For read the user's input in the console, create a variable with value " input({message to show to the user})".
#   The user's input will be store in the variable as string.
      

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
