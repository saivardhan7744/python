# 1. Count Uppercase and Lowercase Letters
# Definition: Uppercase letters are A–Z and lowercase letters are a–z.
# Task: Read a string and print the number of uppercase and lowercase letters.


str1=input("enter the string:")
uppercase=0
lowercase=0
for str in str1:
    if str.isupper():
        uppercase+=1
    elif str.islower():
        lowercase+=1
print(f'Uppercase = {uppercase}')
print(f'Lowercase = {lowercase}')



# 2. Longest Word Length
# Definition: A word is a sequence of characters separated by spaces.
# Task: Read a sentence and print the length of the longest word.


seqCHAR=input("enter the sequence:")
currLENGTH=0
maxLENGTH=0
for ch in seqCHAR:
    if ch !=' ':
        currLENGTH+=1
    else:
        if currLENGTH>maxLENGTH:
            maxLENGTH=currLENGTH
        currLENGTH=0
if currLENGTH>maxLENGTH:
    maxLENGTH=currLENGTH
print(maxLENGTH)



# 3. Count Vowels in Even Positions
# Definition: Vowels are a, e, i, o, u.
# Task: Count vowels present at even index positions.


str1=input("enter the string:")
count=0
for i in range(len(str1)):
    if i%2==0 and str1[i] in 'aeiouAEIOU':
        count+=1
print(count)



# 4. Consecutive Duplicate Characters
# Definition: Consecutive duplicate characters appear one after another.
# Task: Count consecutive duplicate character pairs.


str1=input("enter the string:")
count=0
for i in range(len(str1)-1):
    if str1[i]==str1[i+1]:
        count+=1
print(count)



# 5. First Non-Repeating Character
# Definition: A non-repeating character appears exactly once.
# Task: Print the first non-repeating character or Not Found.


text=input("enter the string:")
for i in text:
    count=0
    for j in text:
        if i==j:
            count+=1
    if count==1:
        print(i)
        break
else:
    print('not found')



# 6. Longest Consecutive Vowel Sequence
# Definition: A vowel sequence is consecutive vowels.
# Task: Find the longest consecutive vowel sequence.


text=input('Enter the string:')
count=0
max=0
for char in text:
    if char in "aeiouAEIOU":
        count+=1
        if count>max:
            max=count
    else:
        count=0
print(max)



# 7. Character Frequency
# Definition: Frequency is the number of occurrences.
# Task: Read a string and a character. Count its occurrences.


str1=input('enter the string:')
char1=input('enter the string:')
count=0
for ch in str1:
    if ch==char1:
        count+=1
print(count)



# 8. Mirror String Check
# Definition: A palindrome reads the same forwards and backwards.
# Task: Check whether the string is a palindrome.


str1=input('enter the string:')
rev=''
for ch in str1:
    rev=ch+rev
if str1==rev:
    print('Palindrome')
else:
    print("not Palindrome")



# 9. Largest Alphabet
# Definition: The largest alphabet has the highest alphabetical order.
# Task: Print the largest alphabet ignoring digits and symbols.


str1=input('enter the string:')
largest_alphabet=0
for ch in str1:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        if ord(ch)>largest_alphabet:
            largest_alphabet=ord(ch)
print(chr(largest_alphabet))



# 10. Compress Consecutive Characters
# Definition: Replace repeated consecutive characters with character followed by count.
# Task: Compress the string.


str2=input("Enter a string: ")
previous=""
count=0
for char in str2:
    if previous=="":
        previous=char
        count=1
    elif char==previous:
        count+=1
    else:
        print(previous, count,sep="",end="")
        previous=char
        count=1
print(previous,count,sep="")