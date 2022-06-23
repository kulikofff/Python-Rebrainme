import this

class names:
    a: int
    b: int

def summ(a, b: names):
    return int(a) + int(b)

a = input("Введите А: ")
b = input("Введите B: ")

print("A + B = ", summ (a,b))
