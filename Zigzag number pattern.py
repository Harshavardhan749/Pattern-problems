# Print a right-aligned number pattern with alternating increasing and decreasing rows.

n=4,m=0,k=0
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end="")
    if i>=1:
        m+=n
        k+=n
    for j in range(1,n+1):
        if m>n:
            o=0
            if i%2==0:
                k=m-(j-1)
                print(k,end=" ")
            else:
                k=k+1
                o=k-1
                print(o,end=" ")
        else:
            print(j,end=" ")
    print()

 
# output:-
#   1 2 3 4 
#  8 7 6 5 
# 9 10 11 12 
#16 15 14 13
