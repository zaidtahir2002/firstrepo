first = input("1st number = ")
second = input("2nd number = ")
operation = input("Operation = ")
if operation == "Add":
	answer = int(first) + int(second)
elif operation == "Subtract":
	answer = int(first) - int(second)
elif operation == "Multiply":
	answer = int(first) * int(second)
elif operation == "Divide":
	answer = int(first) / int(second)
print ("Answer = " + str(answer))
