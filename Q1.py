'''
Write a python program which takes a numeric input and shows how many steps it takes until the Collatz sequence reaches 1.
'''
data = []
step_count = 0
def Collatz(n):
    global step_count
    while n != 1:
        data.append(n)
        if n & 1:
            n = 3 * n + 1
        else:
            n = n // 2
        step_count +=1
    data.append(n)
try:
    n = int(input("Enter numeric value for Collatz sequence: "))
    Collatz(n)
except Exception as e:
    print(f"Error: {e}")
    
print(f"Collatz sequence: {data}")
print(f"Total Step: {step_count}")


