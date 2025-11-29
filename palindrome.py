
def is_palindrome(s):
    return s == s[::-1]

def main():
    s = input("Input word: ")
    if is_palindrome(s):
        print("Word is palindrome")
    else:
        print("Word is not palindrome")

main()