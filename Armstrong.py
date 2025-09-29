#Write a program to check whether the given number is a Armstrong number or not.

def count(num):
    no=0
    while num>0:
        num = num // 10
        no = no + 1
    return no

def isarmstrong(num,no):
    res = 0
    for i in range(0,no):
        a = num % 10
        num = num // 10
        res = res+(a**no)
        a = num
    return res

num = int(input('Enter a numeric number:'))
no = count(num)
res = isarmstrong(num,no)

print(res)

if res == num:
    print(num,'is a Armstrong Number')
else:
    print(num,'is not a Armstrong Number')



