# Python program to implement right angled number pattern.

n=int(input("enter"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    
    if i>=2:
        for j in range(1,i+1):
            if i==j:
                break
            print(i-j,end='')
    print()

"""
output:-
1
121
12321
1234321
123454321
"""
