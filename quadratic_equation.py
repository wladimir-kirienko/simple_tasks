import math

def calc_n_show_qe(a, b, c):
    if not isinstance(a, int) or \
        not isinstance(b, int) or \
        not isinstance(c, int):
        print("Wrong coeffs")
        return

    if a == 0:
        print("Not a quadratic equation (a cannot be 0)")
        return
    
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("No real roots")

def main():
    try:
        s = input("Input a, b, c coeffs (comma separator): ")
        a, b, c = [int(cs) for cs in s.split(',')]
        calc_n_show_qe(a, b, c)
    except:
        print("Input error")

main()



