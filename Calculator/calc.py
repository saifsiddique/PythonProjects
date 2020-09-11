import re


print("Calculator 1.0")
print("Enter q to exit... \n")
choice = True
ans = 0
while(choice):
    prev = ans
    if(prev == 0):
        expression = input("Enter expression: ")
    else:
        expression = input(str(prev))
    if(expression == 'q'):
        choice = False
        print("\nExiting calculator...")
        continue
    re.sub('[a-zA-Z,.:" "]','',expression)
    if(prev == 0):
        ans = eval(expression)
    else:
        ans = eval(str(prev)+expression)
    