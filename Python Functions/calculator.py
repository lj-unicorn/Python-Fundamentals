def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations ={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# print(operations["*"](1,2))


#choose operation





KeepCalculation = True
use_previous = False
calculation = 0
while KeepCalculation:
    if not use_previous:
        num1 = float(input("Enter number \n"))
    else:
        num1 = calculation

    operator = operations[input("Choose operation \n")]
    num2 = float(input("Enter number \n"))
    calculation = operator(num1, num2)
    print(calculation)

    next_step = input(f"Do you want to do operation with previous number {calculation} or begin new? y/n: ")
    if next_step.lower() == "y":
        use_previous = True
    else:
        use_previous = False
