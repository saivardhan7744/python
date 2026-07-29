# 1. Longest Consecutive Consonant Sequence
# Definition: A consonant sequence is a group of consecutive consonants without any vowels in
# between.
# Task: Read a string and print the length of the longest consecutive consonant sequence.


text=input('enter the string:')
currentlength=0
length=0
for char in text:
    if char not in 'aeiou':
        currentlength+=1
        if currentlength>length:
            length=currentlength
    else:
        currentlength=0
print(length)



# 2. Alternate Case Check
# Definition: A string has alternating case if every adjacent pair of letters has different cases.
# Task: Read a string containing only alphabets and determine whether its letters alternate between
# uppercase and lowercase.


s=input("Enter the string:")
for i in range(len(s)-1):
    if ('A'<=s[i]<='Z'and'A'<=s[i+1]<='Z') or ('a'<=s[i]<='z'and'a'<=s[i+1]<='z'):
        print("Not Alternating")
        break
else:
    print("Alternating")



# 3. Most Frequent Character
# Definition: The most frequent character is the one that appears the highest number of times.
# Task: Read a string and print the character with the highest frequency. If there is a tie, print the one
# that appears first.


str=input('enter the string:')
maxcount=0
maxchar=""
for i in str:
    count=0
    for j in str:
        if i==j:
            count+=1
    if count>maxcount:
        maxcount=count
        maxchar=i
print(maxchar)




# 4. Count Words Starting with a Vowel
# Definition: A word starts with a vowel if its first letter is A, E, I, O, or U.
# Task: Read a sentence and count how many words begin with a vowel.

str=input('enter the string:')
count=0
if str[0] in 'aeiouAEIOU':
    count+=1
for i in range(len(str)-1):
    if str[i]==' ' and str[i+1] in 'aeiouAEIOU':
        count+=1
print(count)



# 5. Remove Consecutive Duplicates
# Definition: If the same character appears repeatedly next to itself, keep only one occurrence.
# Task: Read a string and print the modified string.


str=input('enter the string:')
newstr=""
previous=""
for ch in str:
    if ch!=previous:
        newstr+=ch
        previous=ch
print(newstr)
    


# 6. Longest Word
# Definition: The longest word is the word with the maximum number of characters.
# Task: Read a sentence and print the longest word. If multiple words have the same length, print the
# first one.


str=input('enter the string:')
word=''
longWORD=''
for ch in str:
    if ch!=' ':
        word+=ch
    else:
        if len(word)>len(longWORD):
            longWORD=word
        word=''
if len(word) > len(longWORD):
    longWORD = word
print(longWORD)



# 7. Count Character Changes
# Definition: A character change occurs when the current character differs from the previous one.
# Task: Read a string and count how many character changes occur.


str=input('enter the string:')
count=0
for i in range(1,len(str)):
    if str[i]!=str[i-1]:
        count+=1
print(count)



# 8. Rotate String Left by One Position
# Definition: Left rotation moves the first character to the end.
# Task: Read a string and print its left rotation.


str=input("Enter the string: ")
newstr=""
for i in range(1,len(str)):
    newstr+=str[i]
newstr+=str[0]
print(newstr)



# 9. Largest Alphabetical Word
# Definition: The largest alphabetical word is the word that comes last in dictionary order.
# Task: Read a sentence and print the largest alphabetical word.


str=input("Enter the sentence: ")
word= ""
large=""
for ch in str:
    if ch!=' ':
        word+=ch
    else:
        if word>large:
            large=word
        word=""
if word>large:
   large=word
print(large)



# 10. Count Palindromic Words
# Definition: A palindromic word reads the same forward and backward.
# Task: Read a sentence and count how many words are palindromes.


str=input("Enter the sentence:")
word=""
count=0
for ch in str+" ":
    if ch!=' ':
        word+=ch
    else:
        rev =""
        for i in range(len(word)-1, -1, -1):
            rev+=word[i]
        if word==rev:
            count+=1
        word=""
print(count)
