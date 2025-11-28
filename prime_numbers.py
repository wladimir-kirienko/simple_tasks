import math

def is_natural_number(n):
    return isinstance(n, int) and n > 0

def is_prime_number(n):
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

def show_prime_numbers(n):
    print("Prime numbers: ")
    for i in range(2, n + 1):
        if is_prime_number(i):
            print(i, end=' ')
    print()

def main():
    while True:
        try:
            n = input("Input max natural number (type 'e' to exit): ")
            if n == 'e':
                break
            n = int(n)    
            if is_natural_number(n):
                if n < 2:
                    print("Natural number is too small")
                    break
                show_prime_numbers(n)
                break
            else:
                print("Not natural number")
        except:
            print("Input error")

main()



