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
        elif "A"<=i<="Z" or "a"<=i<="z":
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
