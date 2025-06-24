#  Built-in Exception Examples
print("\nBuilt-in Exceptions")
try:
    result = '2' + 2
except TypeError as e:
    print("TypeError caught:", e)

try:
    print(spam * 3)
except NameError as e:
    print("NameError caught:", e)

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)

# Syntax Error vs Exception
print("\nSyntax Error vs Exception")
try:
    amount = 10000
    result = amount / 0
except ZeroDivisionError:
    print("Handled ZeroDivisionError: cannot divide by zero")

# Basic Try-Except
print("\nBasic Try-Except")
a = [1, 2, 3]
try:
    print("Second element =", a[1])
    print("Fourth element =", a[3])  
except IndexError as e:
    print("IndexError caught:", e)

#  Try-Except with Else
print("\nTry-Except with Else")
def divide(a, b):
    try:
        result = (a + b) / (a - b)
    except ZeroDivisionError:
        print("a-b resulted in 0")
    else:
        print("Result:", result)

divide(2.0, 3.0)
divide(3.0, 3.0)

#  Try-Except-Finally
print("\nTry-Except-Finally")
try:
    k = 5 // 0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This is always executed")


# User-defined Exception
print("\nUser-defined Exception")
class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

try:
    salary = int(input("Enter salary amount: "))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)
    else:
        print("Salary is within the valid range.")
except SalaryNotInRangeError as e:
    print("Custom Exception caught:", e)
