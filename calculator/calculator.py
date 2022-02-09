print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')

num1=int(input("enter the value1: "))
num2=int(input("enter the value2: "))
opr=input("Enter the operator like (+ ,- ,* , / ) : ")

if opr=="+":
    print(num1 + num2)
elif opr=="-":
    print(num1 - num2)
elif opr=="*":
    print(num1 * num2)
elif opr=="/":
    print(num1 / num2)
else:
    print("Invalid operation....")