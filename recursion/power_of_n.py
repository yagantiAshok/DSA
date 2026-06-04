




# def power(x,n):

#     if (n==0):

#         return 1
    
#     return x * power(x,n-1)



# print(power(2,17))


# def power_trick(x,n):

#     if n==0:

#         return 1
    
#     half = power_trick(x,n//2)

#     if n%2==0:

#         return half*half
    
#     return x*half*half


# print(power_trick(2.0000,-2))


# def countdigits(num):

#     num = abs(num)

#     if (num>=0 and num<=9):

#         return 1
    
#     digit = num//10

#     return 1 + countdigits(digit)

# print(countdigits(-32134567891))


def countdigits(num):

    num = abs(num)

    if (num>=0 and num<=9): # if (num<10)

        return num
    
    remainder = num%10
    
    digit = num//10

    return remainder + countdigits(digit)

print(countdigits(32134567891))





