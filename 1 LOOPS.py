# 1. Count Passing Students
# Task: Read marks of N students. Count how many scored 35 or more.

students=int(input('enter number of students:'))
count=0
for i in range(1,students+1):
    marks=int(input('enter your marks:'))
    if marks>=35:
        count+=1
print(count)



# 2. Shop Profit Days
# Task: Read profit for N days. Count days with profit greater than Rs.1000.

days=int(input('enter number of days:'))
count=0
for i in range(1,days+1):
    profit=int(input(f'enter your day {i} profit:'))
    if profit>1000:
        count+=1
print(count)



# 3. Largest Multiple of 5
# Task: Read N numbers. Print the largest divisible by 5, else 'No Multiple of 5'.

numbers=int(input('Enter the no.of values:'))
largest=-1
for number in range(1,numbers+1):
    num=int(input('Enter the number:'))
    if num%5==0:
        if num>largest:
            largest=num
if largest==-1:
    print('no multiples of 5')
else:
    print(f'the largest multiple of 5 is: {largest}')



# 4. Average of Even Numbers
# Task: Read N numbers. Print average of even numbers, else 'No Even Numbers'.

numbers=int(input('Enter the no.of values:'))
sum=0
count=0
for number in range(1,numbers+1):
    num=int(input('Enter the numbers:'))
    if num%2==0:
        sum+=num
        count+=1
if count>0:
    avg=sum/count
    print(avg)
else:
    print('no avg number')



# 5. Student Improvement
# Task: Read marks in N tests. Count how many times marks increased.

tests=int(input('enter number of tests:'))
count=0
prevMarks=int(input("Enter the marks: "))
for test in range(2,tests+1):
    marks=int(input(f'enter your test {test} marks:'))
    if marks>prevMarks:
        count+=1
        prevMarks=marks
print(count)



# 6. Divisors Count
# Task: Read a number and count its divisors.

numbers=int(input('Enter the number:'))
count=0
for num in range(1,numbers+1):
    if numbers%num==0:
        count+=1
print(count)



# 7. Smallest Odd Number
# Task: Read N numbers. Print smallest odd number or 'No Odd Number'.

numbers=int(input('Enter the number:'))
smallest=0
for number in range(1,numbers+1):
    num=int(input('enter your numbers:'))
    if num%2!=0:
        if smallest==0 or num<smallest:
            smallest=num
if smallest>0:
    print(f'the smallest odd number is : {smallest}')
else:
    print('no odd numbers')



# 8. Count Numbers Ending with 7
# Task: Read N numbers. Count numbers ending with digit 7.

numbers=int(input('enter number of values:'))
count=0
for number in range(1,numbers+1):
    num=int(input('enter the numbers:'))
    if num%10==7:
        count+=1
print(count)



# 9. Multiplication Table
# Task: Read a number and print table from 1 to 15.

number=int(input('enter the numbers:'))
for i in range(1,16):
    print(f'{number} X {i} = {number*i}')



# 10. Sum Until Negative Number
# Task: Read numbers until a negative number is entered. Print sum of positive numbers.

sum=0
while True:
    num=int(input("Enter a number: "))
    if num < 0:
        break
    sum+=num
print(sum)

