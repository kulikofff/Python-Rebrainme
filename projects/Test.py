def input(n1, n2):
    sum = n1 + n2
    return

print(input(1,2)) 

def pas(n1, n2):
    pass

#print(pas)

def kwarg(n1, n2, kwarg1='default1', kwarg2='default2'):
    print(n1, n2)
    print(kwarg1, kwarg2, end='\n\n')

kwarg(1,2, kwarg1 = 3, kwarg2 = 4)