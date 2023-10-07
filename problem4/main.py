def palindrome(input_string):
    input_string = input_string.replace(" ", "")
    reversed_string = input_string[::-1]

    return input_string == reversed_string


if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False