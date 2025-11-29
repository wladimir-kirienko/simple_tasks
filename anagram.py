
def is_anagram(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))

def main():
    s1 = input("Input first word: ")
    s2 = input("Input second word: ")
    
    if is_anagram(s1, s2):
        print("Words are anagrams")
    else:
        print("Words are not anagrams")

main()