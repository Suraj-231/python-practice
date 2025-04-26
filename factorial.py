number=int(input("enter the number: "))

factorial=1

if (number==0):
    print("factorial of {} is {}".format(number,factorial))
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("factorial of {} is {}".format(number,factorial))
