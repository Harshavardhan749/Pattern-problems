# This program generates a number triangle using nested loops and arithmetic operations based on the input value.

n=int(input("Enter number")) #n=5
k=1,l=0
for i in range(1,n+2):
    for j in range(0,i):
        if i==1:
            print(i,end="")
            break
        if j==0:
            print(k,end=" ")
            l=k
        else:
            l-=(n-(j-1))
            print(l,end=" ")
    k+=((n+1)-i)
    print() 

"""
out put for this program
1
6 1 
10 5 1 
13 8 4 1 
15 10 6 3 1 
16 11 7 4 2 1"""
  
