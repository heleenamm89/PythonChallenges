# Student Mark

print ('------------------')
print ('Student MarkSheet')
print ('------------------')

sub1 = 90
sub2 = 98
sub3 = 85
sub4 = 78
sub5 = 92

Total = sub1 + sub2 + sub3 + sub4 + sub5
Percent = (Total/500) * 100

print ('Total Marks = ',Total,'/ 500')
print ('Percentage = ',Percent,'%')

if Percent > 90 and Percent < 100:
    print('Student Grade =  A+')
elif Percent > 80 and Percent < 90:
    print('Student Grade =  A')
elif Percent > 70 and Percent < 80:
    print('Student Grade =  B')
elif Percent > 60 and Percent < 70:
    print('Student Grade =  C')
elif Percent > 50 and Percent < 60:
    print('Student Grade =  D')
else:
    print('FAIL')