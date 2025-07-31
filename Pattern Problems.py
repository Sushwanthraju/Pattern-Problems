#pattern problems


#Square "*" pattren
rows = 4
cols = 4
for i in range(rows):
    for j in range(cols):
        print("*",end=" ")
    print()




#Square "num" pattren
n = 4
for i in range(n):
    for j in range(n):
        print(i+1,end=" ")
    print()


    

n = 4
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()




#right angle triangle.
n=5
for i in range(1,n+1):
    print("* "*i)



#Reverse right angle triangle.
n=5
for i in range(n,0,-1):
    print("* "*i)



#Triangle.
n=4
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)



#Reverse triangle.
n=4
for i in range(n,0,-1):
    print(" "*(n-i) + "* "*i)




#Hallow square.

rows = 4
cols = 4

for i in range(rows):
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols- 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



    

#down_Right-angle triangle with num.
n=4
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()

#up_Right-angle triangle with num.
n=4
for i in range(n):
    for j in range(n):
        if j < i:
            print(" ",end=" ")
        else:
            print(j+1,end=" ")
    print()

#o/p== 1 2 3 4
#        2 3 4 
#          3 4 
#            4 


#down_Right-angle triangle with num.

n=4
for i in range(n):
    for j in range(n):
        if j < i+1:
            print(j+1,end=" ")
        else:
            print(" ",end=" ")
    print()




    



    
