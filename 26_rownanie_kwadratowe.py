import math


def is_int(param):
    try:
        param = int(param)
    except (TypeError, ValueError):
        print(f"{param} is not a integer!")
    return param
        

def square_equation():
    '''This function is counting square equation'''

    x1 = None
    x2 = None
    
    while True:
        a = input("a parameter:\t")
        b = input("b parameter:\t")
        c = input("c parameter:\t")
        a = is_int(a)
        b = is_int(b)
        c = is_int(c)
        if (type(a) and type(b) and type(c)) != int:
            print("Error end of script")
            break
        else:
            print()
            print("Your params".center(60), "\n", "-"*60)
            print(f'''a = {a}
b = {b}
c = {c}
''')
        if a == 0:
            print("a can not be 0!")
            break
        
        delta = math.pow(b, 2) - (4*a*c)
        
        
        if delta < 0:
            print("Delta can not be less than 0!")
            break

        elif delta == 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            return (x1, x2)

        else:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            return (x1, x2)
            
        
            
        
print(square_equation())
