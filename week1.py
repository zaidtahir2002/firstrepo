first = input("1st number = ")
second = input("2nd number = ")
operation = input("Operation = ")
if operation in ["Add", "add", "+"]:
	answer = float(first) + float(second)
elif operation in ["Subtract", "subtract", "-"]:
        answer = float(first) - float(second)
elif operation in ["Multiply", "multiply", "*"]:
	answer = float(first) * float(second)
elif operation in ["Divide", "divide", "/"]:
	answer = float(first) / float(second)
print ("Answer = " + str(answer))
