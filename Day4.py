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