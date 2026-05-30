def merge_list(l,n):
    out=l
    for i in n:
        out.append(i)
    return out
l=eval(input("enter l1 : "))
n=eval(input("enter l2 : "))
print(merge_list(l,n))