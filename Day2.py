# DAY-2 STRING PROGRAMS
#to reverse the string using two pointer
def rev_str(s):
    l=list(s)
    i=0
    j=len(l)-1
    while i<j:
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1
    return "".join(l)
s=input("Enter a string: ")
print(rev_str(s))

#To check the string palindrome or not using two pointer
def palindrome(s):
    i=0
    j=len(s)-1
    flag=True
    while i<j:
        if s[i]!=s[j]:
            flag=False
            break
        i=i+1
        j=j-1
    if flag:
        return "Palindrome"
    else:
        return "Not Palindrome"
s=input("enter the string : ")
print(palindrome(s))

#to the count of vowels and consonants in a given string
def count_char(s):
    consonant=0
    vowel=0
    for i in s:
        if i in "AEIOUaeiou":
            vowel=vowel+1
        elif "A"<=i<="Z" or "a"<=i<="z": #it is indicated character in A-to-Z
            consonant=consonant+1
    return f"the string contains vowels {vowel} and the consonants {consonant}"
s=input("enter the string : ")
print(count_char(s))

#to occurrence of element in given string
def occur_element(s):
    count=0
    element=input("enter the element : ")
    for i in s:
        if i==element:
            count=count+1
    return count
s=input("enter the string : ")
print(occur_element(s))

#To occurrence of sub-string by the given string
def occur_substr(s,sub):
    count=0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            count=count+1
    return count
s=input("Enter a string: ")
sub=input("Enter a sub string: ")
print(occur_substr(s,sub))

#to remove the space's from the given string
def remove_space(s):
    res=""
    for i in s:
        if i!=" ":
            res+=i
    return res
s=input("Enter a string: ")
print(remove_space(s))

#to rotate the string
def rotation_str(s1,s2):
    if len(s1) == len(s2) and s2 in (s1+s1):
        print("rotation of string")
    else:
        print("no a rotation of string")
s1=input("enter first string : ")
s2=input("enter second string : ")
rotation_str(s1,s2)

#to insert the sub-string into the main string from the given index number
def add_substr(s,sub,ind):
    if ind<0 or ind>len(s):
        return "invalid index"
    else:
        new_s = s[:ind] + sub + s[ind:]
        return new_s
s=input("enter main string : ")
sub=input("enter sub string : ")
ind=int(input("enter index : "))
print(add_substr(s,sub,ind))

#to print largest palindrome sub-string for the given string
def large_palindrome(s):
    large=""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub=s[i:j]
            if sub==sub[::-1] and len(sub)>len(large):
                large=sub
    return large
s=input("Enter a string: ")
print(large_palindrome(s))

#To find the duplicate characters from given string
def duplicate_char(s):
    dup=''
    res=''
    for i in s:
        if i in res:
            dup=dup+i
        else:
            res=res+i
    return dup
s=input("Enter a string : ")
print(duplicate_char(s))

#To find the largest word from the given string
def large_word(s):
    word=s.split()
    large=''
    for i in word:
        if len(i)>len(large):
            large=i
    return large
s=input("Enter a string: ")
print(large_word(s))

#To check the string is anagram or not
"""(anagram : if the both strings are having same characters in any order is called anagram.)"""
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "The strings are anagrams"
    else:
        return "The strings are not anagrams"
s1=input("Enter a string: ").lower().replace(" ","")
s2=input("Enter another string: ").lower().replace(" ","")
print(anagram(s1,s2))

#To check the string is pangram or not
"""A pangram (Greek for "every letter") is a sentence or string of text that contains every single letter of the alphabet at least once."""
def pagram(s):
    import string
    str_set=set(s)
    alpha=set(string.ascii_lowercase)
    if alpha.issubset(str_set):
        return "The strings are anagrams"
    else:
        return "The strings are not anagrams"
s=input("Enter a string: ").lower()
print(pagram(s))

#To find non-repeating character from string
def non_repeat(s):
    for i in range(len(s)):
        c=0
        for j in range(len(s)):
            if s[i]==s[j]:
                c=c+1
        if c==1:
            return s[i]
s=input("Enter a string: ")
print(non_repeat(s))
            #or
def first_non_repeat(s):
    for char in s:
        # Check if the character appears exactly once in the string
        if s.count(char) == 1:
            return char
    return "No unique characters found"

s = input("Enter a character: ")
print(first_non_repeat(s))

"""--------------------------ASSIGNMENT------------------------------"""
# 1. wap to convert lowercase char to uppercase char without using upper()
def convertion(s):
    res = ""
    for ch in s:
        if 'a'<=ch<='z': #it is indicated character in A-to-Z
            res +=chr(ord(ch)-32)
        else:
            res += ch
    return res
s = input('enter a string: ')
print(convertion(s))

# 2. wap to find frequency of each char from given str
def freq(s):
    char = {}
    for i in s:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    return char
s = input('enter a string: ')
print(freq(s))

# 3. wap to remove duplicate char from given str
def duplicate(s):
    res = ''
    for i in s:
        if i in res:
            pass
        else:
            res += i
    return res
s = input('enter a string: ')
print(duplicate(s))

# 4. wap to reverse each word from given str
def reverse_str(s):
    words = s.split()
    result = []
    for i in words:
        result.append(i[::-1])
    return " ".join(result)
s = input('enter a string: ')
print(reverse_str(s))

# 5. wap to reverse the order of str
def reverse_word(s):
    words = s.split()
    reverse_words = reversed(words)
    return " ".join(reverse_words)
s = input('enter a string: ')
print(reverse_word(s))

# 6. wap to store each word into list from the given str without using the split()
def store_words(s):
    words = []
    word = ""
    for ch in s:
        if ch != " ":
            word += ch
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)
    return words
s = input('enter a string: ')
print(store_words(s))

# 7.wap to count upper,lowercase,digit,special symbol,spaces and word from given string
def count_sym(s):
    upper = lower = digit = symbol = space = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isspace():
            symbol += 1
        else:
            symbol += 1
    word = space+1 if s.strip() else 0
    print("uppercase :", upper)
    print("lowercase :", lower)
    print("digits :", digit)
    print("symbols :", symbol)
    print("spaces :", space)
    print("words :", word)
s = input('enter a string: ')
print(count_sym(s))

# 8.wap to print second word from the given str
def second_word(s):
    words = s.split()
    if len(words) >=2:
        return words[1]
    else:
        return "no word found"
s = input("enter a string: ")
print(second_word(s))

# 9.wap to get the following o/p
# i/p = 'python is fun'
# o/p = {'python':6 'is':2 'fun':3}
def word_length_dict(s):
    result = {}
    words = s.split()
    for w in words:
        result[w] = len(w)
    return result
s = input("enter a string: ")
print(word_length_dict(s))