# Variables, Operators and User's Inupt

## Tables Of Content
- [Variables](#variables)
    - [Naming Convention](#naming-convention)
    - [Types](#types)
    - [Types Conversion](#conversions)
- [Operators](#opearators)
    - [Numerics](#numerics)
    - [Strings](#strings)
    - [Booleans](#booleans)
    - [Comparison](#comparison)
- [User's Input](#users-input)

---

## Variables
In python, variable are mutables. A variable containning an int can be replace by another type.
```python
my_int_variable = 10 # My variable contain an int
print(type(my_int_variable)) # => { class 'int' }
my_int_variable = "Hello World" # My variable now contain a string
print(type(my_int_variable)) # => { class 'str' }
```
    
### Naming Convention :
In python, variables and methodes names must respect the "Snake Case" convention.  
Each world must be lowercased and seperated with an underscore.  
    
    ex: my_variables_name

### Types :
- **int** : Integer number
- **flaot** : Decimal number
- **str** : String of characters
- **bool** : True or False value

### Conversions :
For convert a typoe into another equivalent, use the type constructor.  
If the conversion is impossible, the program will emit an error.
```python
# Conversion ok
my_int_variable = 10
my_string_variable = str(my_int_variable) # => "10"

# conversion failed
my_string_value = "hello world"
my_int_value = int(my_string_value) # => not possible! Error!
```

---

## Opearators
### Numerics :
- **+** : Make an addition
- **-** : Make an substraction
- **\*** : Make a multiplication
- **/** : Make a division
### Strings :
 - **+** : Conquer strings. WARNING : You can't conquer string with other types!
 - **\*** : Print as many time as the operand the string
### Booleans :
- **and** : Return True if and only if all variables are True 
- **or** : Return True if one or more variables are True
- **not** : Placed before the value, it return the inverse of the value
### Comparison :
- **==** : Return True if the first value is equal to second value
- **!=** : Return True if first value is different than the second value
- **>** : Return True if the first value is biger than de second value
- **<** : Return True if the first value is smaller than the second value
- **>=** or **<=** : Return True if the first value is *bigger/smaller* Or equal than the second value

```python
# Numerics
addition = 10 + 10 # => 20
substraction = 20 - 10 # => 10
multiplication = 5 * 2 # => 10
division = 10 / 2 # => 5

# Strings
conqered_strings = "Hello" + "World" # => HelloWolrd
multiplyed_stringd = "Hello" * 3 # => HelloHelloHello

# Booleans
and_op = True and False # => False
or_op = True and False # => True
not_op = not False # => True

# Comparisons
equal_comp = 10 == 10 # => True
dif_comp = 10 != 10 # => False
bigger_comp = 10 > 15 # => False
smaller_comp = 10 < 15 # => True
```

---

## User's Input

For read the user's input in the console, create a variable with value " input({m essage to show to the user })".  
The user's input will be store in the variable as string.

```python
user_input = input("What's your name? : ") # => User type "Mick"
print("Your name is : " + user_input) # => Your name is : Mick
```
---