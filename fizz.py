n=int(input("Enter the value of n:\n"))
i=1
while(i<n):
    if(i%3==0 and i%5==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)
    i=i+1