# Write a program to print a triangular number pattern using nested loops and arithmetic operations.

n=int(input("enter")) #n=10
k=0
for i in range(1,n):
    
    for j in range(1,i+1):
        if i==0:
            print(i)
        if j==1:
            k=j
        print(k-((n+1)-j),end="")
    k+=(n-i)
    print()

'''
output:-
1
-9
-9-8
-9-8-7
-9-8-7-6
-9-8-7-6-5
-9-8-7-6-5-4
-9-8-7-6-5-4-3
-9-8-7-6-5-4-3-2
-9-8-7-6-5-4-3-2-1
'''
