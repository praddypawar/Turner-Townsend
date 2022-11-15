des = '''
Fifth supports the following arithmetic operators:
+ - * /
Each of these applies the operator to the two values on the top of the stack and pushes the result to the top of the stack. If division results in a non-integer, round down.

Fifth also supports the following commands:
PUSH x - push x onto the top of the stack, where x is a valid integer
POP - remove the top element of the stack
SWAP - swap the top two elements of the stack
DUP - duplicate the top element of the stack
EXIT  - for Exit
'''
print(des)
print("*"*100)
stack = []
print(f"Stack is: {stack}")
while True:
    try:
        val = input("Enter Command and value: ")
        command = str(val).split(" ")[0]
        print(command)
        if command == "+":
            if len(stack)>=2:
                f_val = stack[-1]
                s_val = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(f_val+s_val)
                print(f"Stack is: {stack}")
            else:
                print("Error")
        elif command == "-":
            if len(stack)>=2:
                f_val = stack[-1]
                s_val = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(f_val-s_val)
                print(f"Stack is: {stack}")
            else:
                print("Error")
        elif command == "*":
            if len(stack)>=2:
                f_val = stack[-1]
                s_val = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(f_val*s_val)
                print(f"Stack is: {stack}")
            else:
                print("Error")
        elif command == "/":
            if len(stack)>=2:
                f_val = stack[-1]
                s_val = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(int(s_val/f_val))
                print(f"Stack is: {stack}")
            else:
                print("Error")
        elif command == "PUSH":
            try:
                val =  str(val).split(" ")[1]
                stack.append(int(val))
                print(f"Stack is: {stack}")
            except Exception as e:
                print(f"Error: {e}")
        elif command == "POP":
            stack.pop()
            print(f"Stack is: {stack}")
        elif command == "DUP":
            f_val = stack[-1]
            stack.append(f_val)
            print(f"Stack is: {stack}")
        elif command == "SWAP":
            f_val = stack[-1]
            s_val = stack[-2]
            stack.pop()
            stack.pop()
            stack.append(f_val)
            stack.append(s_val)
            print(f"Stack is: {stack}")
        elif command.lower() == "exit":
            print(f"Stack is: {stack}")
            break
    except Exception as e:
        print(f"Error: {e}")