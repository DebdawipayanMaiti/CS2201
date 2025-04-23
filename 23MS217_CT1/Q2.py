#Taking the input from the user for cake.
n=int(input("Enter the no. of dickes in cake(n>1): "))
#printing the candle
print(".")
print("|")
#for loop to iterate over and to print % and 
for i in range(1,2*n+1):
    if i%2==0:
        for j in range(1, 2*i):
            print("%",end="")
    else:
        for j in range(1, i):
            print(";",end=" ")
    print()
print("%"*(2*n-1),end="")




        
        
        

