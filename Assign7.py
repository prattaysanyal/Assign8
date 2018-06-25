#question1
x=10
for i in range(x):
    y=int(input("enter the element"))
    print(y)
    
#question2

#question3
l=[]
x=int(input("enter first element"))
y=int(input("enter second element"))
z=int(input("enter third element"))
l.append(x)
l.append(y)
l.append(z)
print(l)
l1=[]
for i in l:
    n=i*i
    l1.append(n)

print(l1)

#question4
l=[2,3,"red","orange",7.6,9.8]
l_int=[]
l_str=[]
l_float=[]
for i in l:
    if(type(i)==int):
        l_int.append(i)
    elif(type(i)==str):
        l_str.append(i)
    elif(type(i)==float):
        l_float.append(i)
print("interger list is :"+str(l_int))
print("string list is :"+str(l_str))
print("float list is :"+str(l_float))


#question5
l=[]
l1=[]
for i in range(1,101):
    if(i%2==0):
        l.append(i)
    else:
        l1.append(i)
print(l)
print(l1)

#question6
x=0
while(x<5):
    print("*"*x)
    x=x+1

#question7
x=int(input("enter value"))
y=int(input("enter second value"))
z=int(input("enter third value"))
dict={"first":x,"second":y,"third":z}
print(dict)
for i in dict:
    print(i,":",dict[i])

#question8
x=int(input("enter the number of elements:"))
l=[]
for i in range(0,x):
    y=int(input("enter elements"))
    l.append(y)
z=int(input("enter element to delete"))
for j in l:
    if(j==z):
        print("element found")
        l.remove(j)
        print(l)
    else:
        print(" not found")


    

    

