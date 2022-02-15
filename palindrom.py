def check_palindrome(data):
    actual_string = data
    reverse = data[::-1]
    if reverse == actual_string:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_word = "sowparnika"
    result = check_palindrome(input_word.lower())
    if result :
        print ("Given word {} is a palindrome".format(input_word))
    else:
        print ("Given word {} is not a palindrome".format(input_word))
