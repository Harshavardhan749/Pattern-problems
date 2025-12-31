# Program to draw dimond shape with asterisks "*" 

n=int(input("Enter the number of rows: "))  # n=5
k=n*2
for i in range(1,k+1):
  
        if i<n:
            print(" "*(n-i)+("*"+" ")*i)
            
        elif i==n:
            print("* "*n)
        else:
            print(" "*(i-n)+"* "*(k-i))
            
# output:-
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
