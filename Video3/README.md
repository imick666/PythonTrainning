# Condition if ... elif ... else

An "if" statement is used to do differents things depending of conditions.  

## Syntax

In python, block as functions, loops, etc are delimited by indentations.

```python
if { condition }:
    # I'm in the scop of my if loop
# I'm out of the scope of my if loop
```

## Usage

- **if** : The first condition of the statement
- **elif** : the others conditions
- **else** : the statement if no conditions passed

```python
# Ask the user his age
age = input("How old are you? : ")

# If the user is older than 18
if age >= 18:
    print("You're major")
    print("You can come in")
# If the user is between 0 and 18
elif age > 0 and age < 18:
    print("You're minor")
    print("You can't come in")
# If the user is 0 year old
elif age == 0:
    print("Welcome on earth!")
# If the user's age doesn't meet any of the previous conditions
else:
    print("which strange age...")

# Out of the if. it will always be print
print("See you")
```


