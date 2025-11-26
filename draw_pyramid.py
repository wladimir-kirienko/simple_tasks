


def draw_pyramid(base = 5):
    half = base // 2

    for i in range(0, half + 1):
        print(' ' * (half - i) + '*' * 2 * i + '*', end='')
        print()

def main():
    draw_pyramid(10)
    
main()