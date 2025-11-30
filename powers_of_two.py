
def is_natural_number(n):
    return isinstance(n, int) and n > 0

def show_powers_of_two(n):
    for i in range(1, n + 1):
        print(2**i, end=' ')
    print()

def main():
    while True:
        try:
            n = input("Input max power of two: (type 'e' to exit): ")
            if n == 'e':
                break
            n = int(n)
            if is_natural_number(n):
                show_powers_of_two(n)
                break
            else:
                print("Not natural number")
        except:
            print("Input error")

main()
