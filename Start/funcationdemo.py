# 1st:Greet
def greet(name):
    print("Hello ",name)

# 2nd:Addition
def addition(a,b):
    return a+b

def main():
    name1 = input("Enter you name:\n")
    greet(name1)
    name2 = input("Enter you name:\n")
    greet(name2)
    num1 = int(input("Enter the 1st number:\n"))
    num2 = int(input("Enter the 2nd number:\n"))
    result = addition(num1,num2)
    print("The result is",result)
main()
    

