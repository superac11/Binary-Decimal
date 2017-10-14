#### Programmer: Sagar Acharya
#### Intro: Program for converting binary to decimal and viceversa.
#### 

print('\t\tEnter the number Choice')
print('\t\t1, For Binary to Decimal')
print('\t\t2, For Decimal to Binary')
print('\t\t---Any other Key for Exit----')

inp=input('Your Choice: ')

if inp=='1':
    num1=input('\nEnter the number in Binary: ')
    decimal=int(num1,2)
    print('Decimal of',num1,'is', decimal)



elif inp=='2':
    num2=int(input('\nEnter the number in Decimal: '))
    decimal=int(num2)
    print('Binary of',num2,'is', bin(num2))


else:
    print('\n\t\t\t\tExiting Program')
    import sys
    sys.exit(1)    
    
