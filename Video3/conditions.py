
age = input("How hold are you? : ")

if age >= 18:
    print("You're major")
    print("You can come in")
elif age > 0 and age < 18:
    print("You're minor")
    print("You can't come in...")
elif age == 0:
    print("Welcome on earth!")
else:
    print("hhhmmm... which strange age....")
    
print("See you")