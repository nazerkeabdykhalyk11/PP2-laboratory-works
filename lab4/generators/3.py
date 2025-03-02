def divisible34(n):
    result=[]
    for i in range(n):
        if i%3==0 and i%4==0:
            result.append(i)
    return result

n = int(input("Enter a number: "))
k=divisible34(n)
print(k)