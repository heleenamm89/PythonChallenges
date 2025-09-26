#create a list of first 100 numbers, from that list create a list of all even numbers, and create a list of all odd numbers, 
# and create a list of numbers are divisible by both 5 & 3.

evennum =[]
oddnum=[]
divby5=[]
divby3=[]
for i in range(1,100):
    if i % 2 == 0:
        evennum.append(i)
    elif i % 2 != 0:
        oddnum.append(i)
    else:
        pass
    if i % 5 == 0:
        divby5.append(i)
    else:
        pass 
    if i % 3 == 0:
        divby3.append(i)
    else:
        pass

print('Even Numbers within range of 1 to 100:', evennum)
print('Odd Numbers within range of 1 to 100:', oddnum)
print('Numbers which are dividends of 5:', divby5)
print('Numbers which are dividends of 3:', divby3)

