import add
def loop_1():
	while True:
		print("Enter -1 to exit")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")
		
		ch = int(input("Enter choice: "))
		
		if ch == 1:
			print(add.add1(10, 20))
		elif ch == 2:
			print(add.sub1(100, 20))
		elif ch == 3:
			print(add.mul1(10, 20))
		elif ch == 4:
			print(add.div1(10, 20))
		elif ch == -1:
			break
loop_1()
