# """Day-4 Dictionary Programming"""

#To find the frequency of the character from string using dictionary
s=input("enter the string : ")
out={}
for i in s: # i : means i travels within s using indexing
    out[i]=s.count(i)   #out[i]:means indexing of out
print(out)

#to merge 2 dictionary
d1=eval(input("enter your first dictionary : "))  #"a":1,"b":2,"c":3}
d2=eval(input("enter your second dictionary : ")) #{"x":24,"y":25,"z":26}
out=d1
for i in  d2:
    out[i]=d2[i] # out[i]: ii this program it means out[i] is a key onside the dictionary
print(out) #{'a': 1, 'b': 2, 'c': 3, 'x': 24, 'y': 25, 'z': 26}

#To sort the dictionary by key
d=eval(input("enter a dictionary : ")) # {"name":"jss","age":21,"course":"PFS","Duration":6}
key=list(d.keys())
for passno in range (1,len(key)):
    for i in range (len(key)-passno):
        if key[i]>key[i+1]:
            key[i],key[i+1]=key[i+1],key[i]
out={}
for i in key:
    out[i]=d[i]
print(out) #{'age': 21, 'course': 'PFS', 'duration': 6, 'name': 'jss'}

#sort the value in dictionary  by value
d=eval(input("Enter the dictionary : ")) #{"a":13,"b":12,"c":76,"d":8,"e":46,"q":2,"f":3,"h":100,"i":33}
items=list(d.items()) #converting dict to list [('a', 13), ('b', 12), ('c', 76), ('d', 8), ('e', 46), ('q', 2), ('f', 3), ('h', 100), ('i', 33)]
for passno in range(1,len(items)):
    for i in range(len(items)-passno):
        if items[i][1]>items[i+1][1]:
            items[i],items[i+1]=items[i+1],items[i]
out={}
for k,v in items: #k=key v=value
    out[k]=v
print(out) #{'q': 2, 'f': 3, 'd': 8, 'b': 12, 'a': 13, 'i': 33, 'e': 46, 'c': 76, 'h': 100}

#to find maximum value in the dictionary
d=eval(input("Enter a dictionary: ")) #{"a":10,"b":38,"c":78,"d":87,"e":198,"q":23,"o":86}
def maximum(d):
    key=list(d.keys())[0]
    max_v=d[key]
    for k,v in d.items():
        if v>max_v:
            max_v=v
            key=k
    return (key,max_v)
print(maximum(d))  #('e', 198)

#to remove duplicate value from the dictionary
d=eval(input("Enter a dictionary: ")) #{"a": 10, "b": 20, "c": 30, "d": 10, "e": 40}
def remove_duplicates(l):
    out={}
    res=set()
    for k,v in d.items():
        if v not in res:
            out[k]=v
            res.add(v)
    return out
print(remove_duplicates(d)) #{'a': 10, 'b': 20, 'c': 30, 'e': 40}

#to access nested dictionary from the given dictionary
