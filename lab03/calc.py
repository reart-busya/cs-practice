num1 = float(input("Первое число >> "))
num2 = float(input("Второе число >> "))
op = str(input("Введите одну из операций: \"+\", \"-\", \"*\" >> "))

def calc(n1, n2, oper):
    if oper == "+":
        return n1 + n2
    if oper == "-":
        return n1 - n2
    if oper == "*":
            return n1 * n2

print(calc(num1, num2, op))