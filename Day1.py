# # DAY-1 LIST PROGRAM
# # 1.find the largest element in the given list
# def largest_val(l):
#     l=list(set(l))
#     l.sort()
#     # return max(l)
#     return f"The largest value of the list is {l[-1]}"
# l=eval(input("enter the number : "))
# print(largest_val(l))
#
# # 2.remove the duplication value from the list
# def duplication(l):
#     out=[]
#     for i in l:
#         if i not in out:
#             out.append(i)
#     return out
# l=eval(input("enter the number : "))
# print(duplication(l))

# # 3. print the second-largest element in the given list
# def second_largest(l):
#     l=list(set(l))
#     l.sort()
#     return f"The second largest number in the given list is {l[-2]}"
# l=eval(input("enter the list : "))
# print(second_largest(l))
# res=second_largest(l)
# print(res)

# # 4 .To merge two list without using "+" operator
# def merge_list(l1,l2):
#     out=l1
#     for i in l2:
#         out.append(i)
#     return out
# l1=eval(input("Enter a list1: ")) # give the input list [1,2,3], not this 1,2,3 because it gives the error
# l2=eval(input("Enter a list2: ")) # give the input list [1,2,3], not this 1,2,3 because it gives the error
# print(merge_list(l1,l2))

# 5. write a program to find the sum of integers present in a given list
def sum_int(l):
    sum = 0
    for i in l:
        if type(i) == int:
            sum=sum+i
    return sum
l=eval(input("enter the number : ")) #[12,3,(1+2j),74,"data",12.7]
print(sum_int(l))


























