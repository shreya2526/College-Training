def reverse(num):
    n = num
    while n > 0:
        print(n % 10, end='')
        n //= 10

reverse(123456)