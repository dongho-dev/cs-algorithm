def palindrome(x):
    x_str = str(x)
    reversed_x_str = x_str[::-1]
    return x_str == reversed_x_str

while True:
    x = int(input())
    if x == 0:
        break;
    
    if palindrome(x):
        print("yes")
    else:
        print("no")
