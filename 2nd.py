num=int(input("Enter Number : "))
result=0
i=2
j=0
while i<num:
    if num%i==0:
        j=j+1
        if j%2==1:
            result=result+(i*10)
        else:
            result=result-(i*10)
    else:
        result=result
    i=i+1
print(result)