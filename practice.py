# 13.WAP to find the pair with given sum
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

