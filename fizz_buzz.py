
def is_natural_number(n):
    return isinstance(n, int) and n > 0

def show_natural_numbers(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz", end=' ')
            else:
                print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
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
                show_natural_numbers(n)
                break
            else:
                print("Not natural number")
        except:
            print("Input error")

main()
