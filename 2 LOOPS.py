# 1. Highest Profit Month
# Definition: Find the maximum value and its position while reading inputs.
# Task: A shop owner records the profit for N months. Print the highest profit and its month number.


months=int(input('enter the month:'))
highest_profit=0
month=0
for i in range(1,months+1):
    profit=int(input('enter the profits:'))
    if profit>highest_profit:
        highest_profit=profit
        month=i
print(f'highest profit={highest_profit}')
print(f'month={month}')



# 2. Perfect Square Counter
# Definition: A perfect square is the square of an integer.
# Task: Read N numbers and count how many are perfect squares.


numbers=int(input('enter a number:'))
count=0
for number in range(1,numbers+1):
    num=int(input('enter a number:'))
    root=int(num**0.5)
    if root*root==num:
        count+=1
print(count)



# 3. Sum of Multiples of 7
# Definition: Multiples of 7 are numbers divisible by 7.
# Task: Read A and B. Sum all multiples of 7 between them.


number1=int(input('enter a number1:'))
number2=int(input('enter a number2:'))
total=0
for i in range(number1,number2+1):
    if i%7==0:
        total+=i
print(total)



# 4. Longest Positive Streak
# Definition: A streak is consecutive values satisfying a condition.
# Task: Read N numbers and find the longest positive streak.


num=int(input('enter a number:'))
currentstreak=0
longeststreak=0
for i in range(1,num+1):
    num1=int(input('enter a number:'))
    if num1>0:
        currentstreak+=1
        if currentstreak>longeststreak:
            longeststreak=currentstreak
    else:
        currentstreak=0
print(longeststreak)



# 5. Count Numbers with Exactly Three Divisors
# Definition: Some numbers have exactly three positive divisors.
# Task: Read N numbers and count them.


num=int(input('enter a number:'))
count=0
for i in range(1,num+1):
    number=int(input('enter a number:'))
    divisors=0
    for j in range(1,number+1):
        if number%j==0:
            divisors+=1
    if divisors==3:
        count+=1
print(count)



# 6. Largest Difference
# Definition: Difference is the gap between two values.
# Task: Find the largest difference between consecutive inputs.


numb=int(input('enter a number:'))
largestdifference=0
prevNum=0
for i in range(1,numb+1):
    currNum=int(input('enter a number:'))
    if currNum>prevNum:
        diff=currNum-prevNum
    else:
        diff=prevNum-currNum
    if diff>largestdifference:
        largestdifference=diff
    prevNum=currNum
print(largestdifference)



# 7. Salary Bonus
# Definition: Employees below a threshold qualify.
# Task: Count salaries below Rs.30000.


employees=int(input('enter the number of employees:'))
count=0
for employee in range(1,employees+1):
    salary=int(input('enter the salary:'))
    if salary<30000:
        count+=1
print(count)




# 8. Largest Digit Sum
# Definition: Digit sum is the sum of all digits.
# Task: Print the number having the largest digit sum.


number=int(input('Enter the number:'))
larg_sum=0
answer=0
for i in range(1,number+1):
    num=int(input('Enter the num:'))
    temp=num
    digit_sum=0
    while temp>0:
        digit=temp%10
        digit_sum+=digit
        temp//=10
    if digit_sum>larg_sum:
        larg_sum=digit_sum
        answer=num
print(answer)



# 9. Average Until Zero
# Definition: Average equals total divided by count.
# Task: Read numbers until 0 and print the average.


total=0
count=0
while True:
    num=int(input('enter a number:'))
    if num==0:
        break
    total+=num
    count+=1
average = total/count
print(f"{average:.2f}")



# 10. Count Numbers Greater Than Average
# Definition: Compare values with the calculated average.
# Task: Read N numbers, compute average, then count numbers above it.


number=int(input('Enter the number:'))
numbers=[]
total=0
for i in range(1,number+1):
    num=int(input('Enter the num:'))
    numbers.append(num)
    total+=num
average=total/number
count=0
for num in numbers:
    if num>average:
        count+=1
print(count)


