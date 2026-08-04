# 1. Remove All Spaces
# Definition: A space (' ') is a blank character between words.
# Task: Remove all spaces from the given string.
# Example Input: Python Programming
# Example Output: PythonProgramming


str1=input("enter the string:")
newWord=''
for ch in str1:
    if ch!=' ':
        newWord+=ch
print(newWord)



# 2. camelCase to snake_case
# Definition: camelCase uses capitals after first word; snake_case uses underscores.
# Task: Convert camelCase to snake_case.
# Example Input: studentName
# Example Output: student_name


str1=input("enter the string:")
snakeCase=''
for ch in str1:
    if ord(ch)>=97:
        snakeCase+=ch
    else:
        snakeCase+='_'+chr(ord(ch)+32)
print(snakeCase)



# 3. snake_case to camelCase
# Definition: snake_case uses underscores; camelCase capitalizes later words.
# Task: Convert snake_case to camelCase.
# Example Input: student_name
# Example Output: studentName


string=input('Enter the snake_case:')
camelcase=''
for i in range(len(string)):
    if string[i]=='_':
        continue
    elif i>0 and string[i-1]=='_':
        camelcase+=chr(ord(string[i])-32)
    else:
        camelcase+=string[i]
print(camelcase)



# 4. Uppercase to Lowercase
# Definition: Uppercase letters are A-Z.
# Task: Convert all uppercase letters to lowercase.
# Example Input: HELLO WORLD
# Example Output: hello world


str1=input('enter the string:')
lowercase=''
for ch in str1:
    if 'A'<=ch<='Z':
        lowercase+=chr(ord(ch)+32)
    else:
        lowercase+=ch
print(lowercase)



# 5. Lowercase to Uppercase
# Definition: Lowercase letters are a-z.
# Task: Convert all lowercase letters to uppercase.
# Example Input: python
# Example Output: PYTHON


str1=input('enter the string:')
uppercase=''
for ch in str1:
    if 'a'<=ch<='z':
        uppercase+=chr(ord(ch)-32)
    else:
        uppercase+=' '
print(uppercase)


# 6. Reverse Every Word
# Definition: Reverse each word only.
# Task: Reverse every word.
# Example Input: Learn Python
# Example Output: nraeL nohtyP


str=input('enter the string:')
rev=''
RevWord=''
for ch in str:
    if ch!=' ':
        rev=ch+rev
    else:
        RevWord=rev+' '
        rev=''
RevWord+=rev
print(RevWord)



# 7. Remove Duplicate Characters
# Definition: Keep first occurrence only.
# Task: Remove duplicate characters.
# Example Input: programming
# Example Output: progamin


str1=input('enter the string:')
newStr=''
for ch in str1:
    if ch not in newStr:
        newStr+=ch
print(newStr)



# 8. Count Vowels and Consonants
# Definition: Count vowels and consonants.
# Task: Print both counts.
# Example Input: Education
# Example Output: Vowels:5 Consonants:4


str1=input('enter the string:')
vowels=0
consonants=0
for ch in str1:
    if ch in 'aeiouAEIOU':
        vowels+=1
    else:
        consonants+=1
print('Vowels=',vowels ,end=' ')
print('Consonants=',consonants)



# 9. Replace Multiple Spaces
# Definition: Extra spaces should become one.
# Task: Replace multiple spaces with one.
# Example Input: Python is fun
# Example Output: Python is fun


str1=input('enter the string:')
newword=''
word=''
for ch in str1:
    if ch!=' ':
        newword+=ch
    else:
        if len(newword)>0 and newword[-1]!=' ':
            newword+=ch
print(newword)



# 10. Capitalize Every Word
# Definition: First letter uppercase.
# Task: Convert to title case.
# Example Input: welcome to python
# Example Output: Welcome To Python


str=input("Enter a string: ")
result = ""
for ch in range(len(str)):
    if ch== 0 and 'a' <= str[ch] <= 'z':
        result = result + chr(ord(str[ch]) - 32)
    elif ch> 0 and str[ch-1] == ' ' and 'a' <= str[ch] <= 'z':
        result = result + chr(ord(str[ch]) - 32)
    else:
        result = result + str[ch]

print(result)



# 11. Print Only Digits
# Definition: Digits are 0-9.
# Task: Extract digits.
# Example Input: AB12CD345
# Example Output: 12345


str1=input('entrer the string:')
newstring=''
for ch in str1:
    if '0'<=ch<='9':
        newstring+=ch
print(newstring)



# 12. Print Only Alphabets
# Definition: Letters only.
# Task: Remove digits and symbols.
# Example Input: Pyt#123hon!
# Example Output: Python


str=input('enter the str:')
newstring=''
for ch in str:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        newstring+=ch
print(newstring)




# 13. Count Words
# Definition: Words separated by spaces.
# Task: Count words.
# Example Input: Python is easy to learn
# Example Output: 5


string=input('Enter the string:')
count=0
for char in range(len(string)):
    if string[char]!=' ':
        if char==0 or string[char-1]==' ':
         count+=1
print(count)



# 14. Check Anagram
# Definition: Same letters, different order.
# Task: Check anagram.
# Example Input: listen / silent
# Example Output: Anagram


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) != len(str2):
    print("Not Anagram")
else:
    flag = True
    for ch in str1:
        c1 = 0
        c2 = 0
        for x in str1:
            if x == ch:
                c1 += 1
        for x in str2:
            if x == ch:
                c2 += 1
        if c1 != c2:
            flag = False
            break
    if flag:
        print("Anagram")
    else:
        print("Not Anagram")



# 15. Find Longest Word
# Definition: Longest word has most characters.
# Task: Print longest word.
# Example Input: I love programming language
# Example Output: programming


str1=input('enter the string:')
word=''
longest=''
for ch in str1:
    if ch!=' ':
        word+=ch
    else:
        if len(word)>len(longest):
            longest=word
        word=''
if len(word)>len(longest):
    longest=word
print(longest)



# 16. Remove All Digits
# Definition: Digits are numeric chars.
# Task: Remove all digits.
# Example Input: Room12Block5
# Example Output: RoomBlock


str1=input('enter the string:')
newSTR=''
for ch in str1:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        newSTR+=ch
print(newSTR)



# 17. Move Digits to End
# Definition: Keep letter order.
# Task: Move digits to end.
# Example Input: A1B2C34
# Example Output: ABC1234


str=input('enter the string:')
digit=''
letters=''
newstr=''
for ch in str:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        letters+=ch
    elif '0'<=ch<='9':
        digit+=ch
newstr=letters+digit
print(newstr)



# 18. Toggle Case
# Definition: Swap upper/lower.
# Task: Toggle every letter.
# Example Input: PyThOn
# Example Output: pYtHoN


str1=input('enter the string:')
Togglestr=''
for ch in str1:
    if 'A'<=ch<='Z':
        Togglestr+=chr(ord(ch)+32)
    else:
        Togglestr+=chr(ord(ch)-32)
print(Togglestr)



# 19. Palindrome
# Definition: Reads same both ways.
# Task: Check palindrome.
# Example Input: madam
# Example Output: Palindrome


string=input("Enter string:")
rev=""
for ch in string:
    rev=ch+rev
if string== rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 20. Compress Characters
# Definition: Consecutive repeats become char+count.
# Task: Compress string.
# Example Input: aaabbccccdd
# Example Output: a3b2c4d2


str1=input('enter the string:')
newStr=''
count=1
for ch in range(1,len(str1)):
    if str1[ch]==str1[ch-1]:
        count+=1
    else:
       newStr+=str1[ch-1]+str(count)
       count=1
newStr+=str1[-1]+str(count)
print(newStr)