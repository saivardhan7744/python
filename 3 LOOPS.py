# 1. Consecutive Pass Count
# Definition: A consecutive pass means students pass one after another without any failure in
# between.
# Task: Read marks of N students and find the longest consecutive sequence of students scoring 35
# or more.


students=int(input('enter number of students:'))
Longest_Consecutive_Passes=0
count=0
for student in range(1,students+1):
    marks=int(input(f'enter the marks of {student}st student:'))
    if marks>=35:
        count+=1
        if count>Longest_Consecutive_Passes:
            Longest_Consecutive_Passes=count
    else:
        count=0
print(f'longest consecutive sequence of students scoring 35 or more is {Longest_Consecutive_Passes}')



# 2. Largest Prime Entered
# Definition: A prime number has exactly two positive divisors.
# Task: Read N numbers and print the largest prime.


numbers=int(input('enter a number:'))
largestPRIME=0
for number in range(1,numbers+1):
    num=int(input('enter a number:'))
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        if num>largestPRIME:
            largestPRIME=num
print(f'largest prime is {largestPRIME}')
    


# 3. Sum of Even Digits
# Definition: Even digits are 0,2,4,6,8.
# Task: Read a number and print the sum of even digits.


number=int(input('enter a number:'))
sum=0
while number>0:
    digit=number%10
    if digit%2==0:
        sum+=digit
    number=number//10
print(f'sum of even digits is {sum}')



# 4. Factory Quality Check
# Definition: Quality below 50 is defective.
# Task: Read N scores and print defective and good counts.


number=int(input('enter a number:'))
defective=0
good=0
for num in range(1,number+1):
    score=int(input('enter your score:'))
    if score<50:
        defective+=1
    else:
        good+=1

print(f'defective = {defective}')
print(f'good = {good}')



# 5. Maximum Sales Increase
# Definition: Increase is today's sales minus yesterday's.
# Task: Find the maximum increase between consecutive days.


days=int(input('enter number of days:'))
previousSALE=int(input('enter todays sale:'))
max=0
for day in range(2,days+1):  #(days-1)
    currentSALE=int(input('enter the sale:'))
    increase=currentSALE-previousSALE
    if increase>max:
        max=increase
    previousSALE=currentSALE
print(f'maximum increase between consecutive days is {max}')



# 6. Number with Most Digits
# Definition: Digit count is the number of digits.
# Task: Print the number with the most digits.


number=int(input('enter a number:'))
answer=0
maxDIGIT=0
for i in range(1,number+1):
    num=int(input('enter a number:'))
    temp=num
    count=0
    while temp>0:
        count+=1
        temp=temp//10
    if count>maxDIGIT:
        maxDIGIT=count
        answer=num
print(f'the number with the most digits = {answer}')




# 7. Count Numbers Divisible by Both 4 and 6
# Definition: Such numbers are divisible by 12.
# Task: Count such numbers.


num=int(input('enter a number:'))
count=0
for i in range(1,num+1):
    number=int(input('enter the number:'))
    if number%12==0:
        count+=1
print(count)



# 8. Longest Odd Streak
# Definition: An odd streak is consecutive odd numbers.
# Task: Find the longest odd streak.


num=int(input('enter a number:'))
count=0
oddSTREAK=0
for i in range(1,num+1):
    number=int(input('enter the number:'))
    if number%2!=0:
        count+=1
        if count>oddSTREAK:
            oddSTREAK=count
    else:
        count=0
print(oddSTREAK)



# 9. Smallest Digit Sum
# Definition: Digit sum is the sum of a number's digits.
# Task: Print the number with the smallest digit sum.


number=int(input('Enter the number:'))
smallest=100000
answer=0
for i in range(1,number+1):
    num=int(input('Enter the num:'))
    temp=num
    total=0
    while temp>0:
        total+=temp%10
        temp=temp//10
    if total<smallest:
        smallest=total
        answer=num
print(answer)


# 10. Running Balance
# Definition: Running balance updates after each transaction.
# Task: Print balance after each transaction and final balance.


balance=int(input('Enter the balance:'))
number=int(input('Enter the no.of trans:'))
for i in range(1,number+1):
    transaction=int(input('Enter the transaction:'))
    balance+=transaction
    print("balance=",balance)
print("final balance=",balance)