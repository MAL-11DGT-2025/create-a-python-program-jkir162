print("Hello, World!")

name = input("What is your name: ")
print(f"Kia ora {name}.")

age = int(input("What is your age: "))

if age > 25:
    print("You are old.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")