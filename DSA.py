"""-------Searching Algorithms for DSA(linear search,binary search,ternary search)--------"""
# def without_temp(n1, n2):
# #Linear Search (Time Complexity:O(n) , Space Complexity:O(1))
# """
# Time complexity measures how the runtime of an algorithm grows relative to the size of the input
# ($n$, which is the number of elements in your collection col).
#  total_time = n XO(1)=O(n)
#
# Space complexity measures the amount of extra memory/space an algorithm allocation requires relative to the input size.
# Because the extra memory requirement is constant and independent of $n$, the Space Complexity is $O(1)$.
# """
# def linear_search(col,key):
#     for i in range(len(col)):
#         if col[i] == key:
#             return i
#     return -1
# col=eval(input("enter your col : "))
# key=int(input("enter your key : "))
# print(linear_search(col,key))
#
# #Binary Search (Time Complexity (TC): O(log n)  Space Complexity (SC): O(1) )
# def binary_search(col,key):
#     low=0
#     high=len(col)-1
#     while low<=high:
#         mid=(low+high)//2
#         if col[mid]==key:
#             return mid
#         elif col[mid]<key:
#             low=mid+1
#         else:
#             low=mid-1
# col=eval(input("enter your collection : "))
# key=int(input("enter your key : "))
# print(binary_search(col,key))
#
# """----------Sorting Algorithms for DSA(bubble sort,selection sort,insertion sort,quick sort,merge sort)--------"""
# """1.Bubble sort Algorithm (Time Complexity : O(n^2) and Space Complexity : O(1))"""
# def bubble_sort(arr):
#     for passnum in range(1,len(arr)):
#         for i in range(0,len(arr)-passnum):
#             if arr[i] > arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1],arr[i]
#     return arr
# arr=eval(input("enter array : "))
# print(bubble_sort(arr))

"""Stack-FILO(first in last out) / LIFO(last in first out)
implement in two ways
1.using python list
2.using in-built module
"""
#using python list
class stack:
    def __init__(self,size=5):
        self.size=size
        self.st=[]
    def push(self,data):
        if len(self.st)==self.size:
            raise ValueError("Stack is full")
        else:
            self.st.append(data)
    def pop(self):
        if len(self.st)==0:
            raise ValueError("Stack is empty")
        else:
            self.st.pop()
    def peek(self):
        return self.st[-1]
    def display(self):
        return self.st
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.push(60)
s.pop()
s.push(70)
print(s.display())
# s.push(7) #error because stack is full

#using in-built module
from collections import deque
st=deque()
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.pop()
print(st)
print(st[-1])
st.pop()
print(st)
#ex:2
st=deque(maxlen=5)
st.appendleft(10)
st.appendleft(20)
st.appendleft(30)
st.appendleft(40)
st.popleft()
print(st)
print(st[-1])

"""Queue : FIFO(first in first out) / LILO(last in last out)
Implement in two ways
1.using python list
2.using in-built module"""
#using python list
class Queue:
    def __init__(self,size=5):
        self.size=size
        self.qu=[]
    def push(self,data):
        if len(self.qu)==self.size:
            raise ValueError("Queue is full")
        else:
            self.qu.append(data)
    def pop(self):
        if len(self.qu)==0:
            raise ValueError("Queue is empty")
        else:
            self.qu.pop(0)
    def peek(self):
        return self.qu[0]
    def display(self):
        return self.qu
q=Queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
q.pop()
print(q.peek()) #20
print(q.display()) #[20, 30, 40, 50]

#2.Using in-built method
from collections import deque
q=deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q) #deque([1, 2, 3, 4, 5])
q.popleft()
print(q) #deque([2, 3, 4, 5])
print(q[0]) #2
ex:2
from collections import deque
q=deque(maxlen=5)
q.append(10)
q.append(20)
q.append(30)
q.append(40)
print(q) #deque([10, 20, 30, 40], maxlen=5)
q.pop()
print(q) #deque([10, 20, 30], maxlen=5)
print(q[-1]) #30

"""Single Linked List"""
class snode:
    def __init__(self,data):
        self.data=data
        self.next=None
    def get_data(self):
        return self.data
    def set_data(self,new):
        self.data=new
    def get_next(self):
        return self.next
    def set_next(self,new):
        self.next=new
n1=snode(10)
n2=snode(20)
n3=snode(30)
n4=snode(40)
n1.set_next(n2)
n2.set_next(n3)
n3.set_next(n4)
ptr=n1
while ptr!= None:
    print(ptr.get_data()) #10,\n20,\n30,\n40
    ptr=ptr.get_next()