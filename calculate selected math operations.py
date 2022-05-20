# 9/21/20
#math
#calculate selected math operations

Num1 = float()
Num2 = float()
Answer = float()
Operation = str()

Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))

# Get Operation
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
Operation = input("\nEnter the number of the desired operation: ")

# Calc Answer
if Operation == "1":
    Answer = Num1 + Num2
elif Operation == "2":
    Answer = Num1 - Num2
elif Operation == "3":
    Answer = Num1 * Num2
else:
    Answer = Num1 / Num2

# Display Answer
print("Answer: ", Answer)
