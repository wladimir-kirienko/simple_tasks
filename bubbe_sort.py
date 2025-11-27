
import random

def bubble_sort(seq):
    def show(seq):
        print(seq)
        input()

    n = len(seq)
    show(seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]   
        show(seq)     

def main():
    n = random.randint(5, 7)
    seq = random.sample(range(1, 11), n)    
    bubble_sort(seq)


main()

