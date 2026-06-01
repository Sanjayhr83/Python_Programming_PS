# DAY-1 LIST PROGRAMS
# 1.find the largest element in the given list
def largest_val(l):
    l=list(set(l))
    l.sort()
    # return max(l)
    return f"The largest value of the list is {l[-1]}"
l=eval(input("enter the number : "))
print(largest_val(l))

# 2.remove the duplication value from the list
def duplication(l):
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
    return out
l=eval(input("enter the number : "))
print(duplication(l))

# only print the duplicate values in the list
def duplicate_val(l):
    duplicate=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j] and l[i] not in duplicate:
                duplicate.append(l[i])
    return duplicate
l=eval(input("Enter a list: "))
print(duplicate_val(l))

# 3. print the second-largest element in the given list
def second_largest(l):
    l=list(set(l))
    l.sort()
    return f"The second largest number in the given list is {l[-2]}"
l=eval(input("enter the list : "))
print(second_largest(l))
res=second_largest(l)
print(res)

# # 4 .To merge two list without using "+" operator
def merge_list(l1,l2):
    out=l1
    for i in l2:
        out.append(i)
    return out
l1=eval(input("Enter a list1: ")) # give the input list [1,2,3], not this 1,2,3 because it gives the error
l2=eval(input("Enter a list2: ")) # give the input list [1,2,3], not this 1,2,3 because it gives the error
print(merge_list(l1,l2))

# # 5. write a program(WAP)  to find the sum of integers present in a given list
def sum_int(l):
    sum = 0
    for i in l:
        if type(i) == int:
            sum=sum+i
    return sum
l=eval(input("enter the number : ")) #[12,3,(1+2j),74,"data",12.7,45]
print(sum_int(l))

# # 6. write a program(WAP) to reverse the list using two pointer
def rev_list(l):
    i=0
    j=len(l)-1
    while i<j:
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1
    return l
l=eval(input("Enter a list: "))
print(rev_list(l))

# # 7.write a program(WAP) to check weather the list is palindrome or not using two pointer
def palindrome(l):
    i=0
    j=len(l)-1
    flag=True
    while i<j:
        if l[i]!=l[j]:
            flag=False
            break
        i=i+1
        j=j-1
    if flag:
        return "Palindrome"
    else:
        return "Not Palindrome"
l=eval(input("Enter a list: "))
print(palindrome(l))

# # 8. WAP to print common elements from the two list
def common_val(l1,l2):
    out=[]
    for i in l1:
        if i in l2 and i not in out:
            out.append(i)
    return out
l1=eval(input("Enter a list1: "))
l2=eval(input("Enter a list2: "))
print(common_val(l1,l2))

# # 9. WAP to find frequency of the elements from the list
def frequency_val(l):
    out = []
    for i in l:
        if i not in out:
            print(i,":",l.count(i))
            out.append(i)
l=eval(input("Enter a list: "))
frequency_val(l)

# # 10.WAP to rotate the list for n number of times to right or left l=list,n=number of list
"""RIGHT-ROTATION"""
def right_rotate(l,n):
    n=n%len(l)
    out=l[-n:]+l[:-n]
    return out
l=eval(input("enter a list : "))
n=int(input("enter a number : "))
print(right_rotate(l,n))
"""LEFT-ROTATION"""
def left_rotate(l,n):
    n=n%len(l)
    out=l[n:]+l[:n]
    return out
l=eval(input("enter a number: "))
n=int(input("enter a number: "))
print(left_rotate(l,n))

# 11.WAP to move zero to end of the list
"""USING ONLY CONDITION STATEMENTS(IF,ELSE,ELIF)"""
l=[1,2,3,0,0,4,5,0]
l1=[]
l2=[]
for i in l:
    if i!=0:
        l1.append(i)
    else:
        l2.append(i)
print(l1)
print(l2)
print(l1+l2)
"""USING FUNCTION"""
def end_lst(l):
    non_zero=[]
    zero=[]
    for i in l:
        if i!=0:
            non_zero.append(i)
        else:
            zero.append(i)
    return non_zero+zero
l=eval(input("enter the number : "))
print(end_lst(l))

# # 12.WAP to find missing number from list(1 to n)
"""ONLY APPLICABLE FOR ONE VALUE MISSING"""
def missing_num(l):
    n=int(input("enter n number : "))
    sum_val=sum(l)
    res=n*(n+1)//2
    return res-sum_val
l=eval(input("enter number : "))
print(missing_num(l))
"""IT IS APPLICABLE FOR MANY MISSING NUMBER"""
l=eval(input("enter number : "))
n = int(input("enter n number : "))
for i in range(1,n+1):
    if i not in l:
        print(i)

# # 13.WAP to find the pair with given sum
"""for example:
    l=[1000,700,100,900,300]
    n=1000
    o/p : [[1000],[700,300],[100,900]]
"""
def sum(l,n):
    out=[]
    for i in range(0,len(l)):
        if l[i]==n:
            out.append([l[i]])#without square bracket it show error because we write output list inside another list
        else:
            for j in range(i+1,len(l)):
                if l[i]+l[j]==n:
                    out.append([l[i],l[j]])
    return out
l=eval(input("enter the list : "))
n=int(input("enter the n value : "))
print(sum(l,n))

"""-----------------LIST PROGRAMS----------------------------"""
# 1. wap to find first repeating elements
def firstrepeating(l):
    seen = []
    for i in l:
        if i in seen:
            return i
        else:
            seen.append(i)
    return "not found"
l = eval(input("Enter a list: "))
print(firstrepeating(l))

# 2. sap to find the index of given element withput using index()
def index(l,target):
    pos = 0
    for i in l:
        if i == target:
            return pos
        pos = pos + 1
    return "not found"
l = eval(input("Enter a list: "))
target = eval(input("Enter a target: "))
print(index(l,target))

# 3. wap to count the occurrence of given element in the given list
def element(l,x):
    count = 0
    for i in l:
        if i == x:
            count = count + 1
    return count
l = eval(input("Enter a list: "))
x = eval(input("Enter a target: "))
print(element(l,x))

# 4.wap to get following o/p
# i/p = ['python.py','pro1.html','data.db','google.com']
# o/p = ['py','html','db','com']
def extensions(l):
    e1=[]
    for i in l:
        parts = i.split(".")
        e1.append(parts[-1])
    return e1
l = eval(input("Enter a list: "))
print(extensions(l))

# 5. wap to extract all the interger which are multiple of 5 and has three digit in it from list
def extract(l):
    e1 = []
    for num in l:
        if num % 5 ==0 and abs(num)>=100 and abs(num)<=999:
            e1.append(num)
    return e1
l = eval(input("Enter a list: "))
print(extract(l))

# 6. wap to split list into even and odd list
def seperate(l):
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
l = eval(input("Enter a list: "))
even,odd =seperate(l)
print(even)
print(odd)

# 7. wap to find duplicate element from the list
def duplicate(l):
    out = []
    for i in l:
        if i not in l:
            out.append(i)
    return out
l = eval(input("Enter a list: "))
print(duplicate(l))

# 8. wap to check whether list is sorted or not
def sorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return "not sorted"
    return "sorted"
l = eval(input("Enter a list: "))
print(sorted(l))

# 9. wap  to find non-repeated element in the list
def repeated(l):
    out = []
    for i in l:
        if l.count(i)==1:
            out.append(i)
    return out
l = eval(input("Enter a list: "))
print(repeated(l))

# 10. wap to find the element which is repeated more number of times
def mostrepeated(l):
    max_count = 0
    max_element = None
    for i in l:
        count = l.count(i)
        if count>max_count:
            max_count = count
            max_element = i
    return max_element,max_count
l = eval(input("Enter a list: "))
element , freq = mostrepeated(l)
print(element,freq)