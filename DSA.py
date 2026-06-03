#Linear Search (Time Complexity:O(n) , Space Complexity:O(1))
"""
Time complexity measures how the runtime of an algorithm grows relative to the size of the input
($n$, which is the number of elements in your collection col).
 total_time = n XO(1)=O(n)

Space complexity measures the amount of extra memory/space an algorithm allocation requires relative to the input size.
Because the extra memory requirement is constant and independent of $n$, the Space Complexity is $O(1)$.
"""
def linear_search(col,key):
    for i in range(len(col)):
        if col[i] == key:
            return i
    return -1
col=eval(input("enter your col : "))
key=int(input("enter your key : "))
print(linear_search(col,key))

